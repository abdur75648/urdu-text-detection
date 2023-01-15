# To run the pre-trained model on one single image
import argparse, os,json
from tqdm import tqdm
from PIL import Image, ImageDraw

import torch
from maskrcnn_benchmark.config import cfg
from maskrcnn_benchmark.data import make_data_loader
from maskrcnn_benchmark.engine.inference import inference
from maskrcnn_benchmark.modeling.detector import build_detection_model
from maskrcnn_benchmark.utils.checkpoint import DetectronCheckpointer
from maskrcnn_benchmark.utils.comm import synchronize, get_rank
from maskrcnn_benchmark.utils.logger import setup_logger
from maskrcnn_benchmark.utils.miscellaneous import mkdir

device = 'cuda' if torch.cuda.is_available() else 'cpu'

if __name__ == "__main__":
    print("Running Inference on './test.jpg...'")
    parser = argparse.ArgumentParser(description="Text Line Detection Inference")
    parser.add_argument( "--config-file", default="inference_config.yaml", metavar="FILE", help="path to config file")
    parser.add_argument("--local_rank", type=int, default=0)
    parser.add_argument( "opts",help="Modify config options using the command-line",default=None,nargs=argparse.REMAINDER)
    args = parser.parse_args()

    num_gpus = int(os.environ["WORLD_SIZE"]) if "WORLD_SIZE" in os.environ else 1
    distributed = num_gpus > 1

    if distributed:
        torch.cuda.set_device(args.local_rank)
        torch.distributed.init_process_group(
            backend="nccl", init_method="env://"
        )
        synchronize()

    cfg.merge_from_file(args.config_file)
    cfg.merge_from_list(args.opts)
    cfg.freeze()

    save_dir = ""
    logger = setup_logger("maskrcnn_benchmark", save_dir, get_rank())
    # logger.info("Using {} GPUs".format(num_gpus))
    
    model = build_detection_model(cfg)
    model.to(cfg.MODEL.DEVICE)
    
    output_dir = cfg.OUTPUT_DIR
    last_checkpoint_file= cfg.LAST_CHECKPOINT_FILE

    checkpointer = DetectronCheckpointer(cfg, model, last_checkpoint_file=last_checkpoint_file,save_dir=output_dir)
    _ = checkpointer.load(cfg.MODEL.WEIGHT)

    
    test_img = Image.open("test.jpg")
    test_w,test_h = test_img.size
    json_dict = {"images": [{"height": test_h,"width": test_w,"id": 0,"file_name": "test.jpg"}],
    "annotations": [],
    "categories": [{"supercategory": "urdu_text","id": 1, "name": "text"}]
    }

    json.dump(json_dict,open("maskrcnn_benchmark/engine/test.json", 'w'), ensure_ascii=False)
    
    iou_types = ("bbox",)
    if cfg.MODEL.BOUNDARY_ON:
        iou_types = iou_types + ("bo",)
    output_folders = [cfg.OUTPUT_DIR]*len(cfg.DATASETS.TEST)
    dataset_names = cfg.DATASETS.TEST



    if cfg.OUTPUT_DIR:
        for idx, dataset_name in enumerate(dataset_names):
            output_folder = "vis"
            mkdir(output_folder)
            output_folders[idx] = output_folder

    data_loaders_val = make_data_loader(cfg, is_train=False, is_distributed=distributed)
    
    for output_folder, dataset_name, data_loader_val in zip(output_folders, dataset_names, data_loaders_val):
        bo = inference(
            model,
            data_loader_val,
            dataset_name=dataset_name,
            iou_types=iou_types,
            box_only=False if cfg.MODEL.FCOS_ON or cfg.MODEL.RETINANET_ON else cfg.MODEL.RPN_ONLY,
            device=cfg.MODEL.DEVICE,
            expected_results=cfg.TEST.EXPECTED_RESULTS,
            expected_results_sigma_tol=cfg.TEST.EXPECTED_RESULTS_SIGMA_TOL,
            output_folder=output_folder,
        )
        synchronize()
    
    bboxes = []
    for detection in bo:
        bboxes.append(detection["seg_rorect"])
    bboxes = sorted(bboxes,key=lambda x:x[1])

    print("\n###Cropping Image###\n")
    image = Image.open("test.jpg")
    for num_box,points in enumerate(tqdm(bboxes)):
        min_x = min(points[0::2])
        max_x = max(points[0::2])
        min_y = min(points[1::2])
        max_y = max(points[1::2])
        im_cropped = image.crop((int(min_x), int(min_y), int(max_x), int(max_y)))
        im_cropped.save(f"vis/{str(num_box+1).zfill(3)}_test.jpg")

    os.remove("maskrcnn_benchmark/engine/test.json")

    print("\n### Completed Inference###")