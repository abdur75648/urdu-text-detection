# Urdu OCR - Text Line Detection Inference

**Released as a supplement of [UTRNet: High-Resolution Urdu Text Recognition](https://github.com/abdur75648/UTRNet-High-Resolution-Urdu-Text-Recognition)**

[![UTRNet](https://img.shields.io/badge/UTRNet:%20High--Resolution%20Urdu%20Text%20Recognition-blueviolet?logo=github&style=flat-square)](https://github.com/abdur75648/UTRNet-High-Resolution-Urdu-Text-Recognition)
[![Website](https://img.shields.io/badge/Website-Visit%20Here-brightgreen?style=flat-square)](https://abdur75648.github.io/UTRNet/)
[![arXiv](https://img.shields.io/badge/arXiv-2306.15782-darkred.svg)](https://arxiv.org/abs/2306.15782)

## Steps to run the code
***Note** - Due to several dependency issues in maskrcnn-benchmark, a dockerizes version has been released*

* Clone the repository
* Download trained model (contourNet_model.pth) from [here](https://csciitd-my.sharepoint.com/:u:/g/personal/ch7190150_iitd_ac_in/EbHAIISEi_xFoB_WFP4z2WwBoit3lZwffrVt5vXyFoQpiQ?e=NgxeVh)
* Run the following commands in the terminal
    * ```docker build -t ocr_docker .```
    * ```docker run -it --name ocr_app -v /Users/abdur/Desktop/cn_inference:/cn_inference ocr_docker```
    * ```cd cn_inference```
    * ```export INSTALL_DIR=$PWD```
    * ```cd $INSTALL_DIR && cd maskrcnn-benchmark && python3 setup.py build develop && cd $INSTALL_DIR```
    * ```unset INSTALL_DIR```
    * ```cp -r maskrcnn-benchmark/maskrcnn_benchmark .```

## Note
The code & trained model is for research purposes only and must not be used for any other purpose without the author's explicit permission.

## Citation
If you use the code/model/dataset, please cite the following paper:

```BibTeX
@article{rahman2023utrnet,
      title={UTRNet: High-Resolution Urdu Text Recognition In Printed Documents}, 
      author={Abdur Rahman and Arjun Ghosh and Chetan Arora},
      journal={arXiv preprint arXiv:2306.15782},
      year={2023},
      eprint={2306.15782},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      doi = {https://doi.org/10.48550/arXiv.2306.15782},
      url = {https://arxiv.org/abs/2306.15782}
}
```

### License
[![Creative Commons License](https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-nc-sa/4.0/). This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/) for Noncommercial (academic & research) purposes only and must not be used for any other purpose without the author's explicit permission.
