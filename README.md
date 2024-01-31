# Urdu OCR - Text Line Detection Inference

**Released as a supplement of [UTRNet: High-Resolution Urdu Text Recognition](https://github.com/abdur75648/UTRNet-High-Resolution-Urdu-Text-Recognition)**

[![UTRNet](https://img.shields.io/badge/UTRNet:%20High--Resolution%20Urdu%20Text%20Recognition-blueviolet?logo=github&style=flat-square)](https://github.com/abdur75648/UTRNet-High-Resolution-Urdu-Text-Recognition)
[![Website](https://img.shields.io/badge/Website-Visit%20Here-darkgreen?style=flat-square)](https://abdur75648.github.io/UTRNet/)
[![arXiv](https://img.shields.io/badge/arXiv-2306.15782-darkred.svg)](https://arxiv.org/abs/2306.15782)
[![SpringerLink](https://img.shields.io/badge/Springer-Page-darkblue.svg)](https://link.springer.com/chapter/10.1007/978-3-031-41734-4_19)
[![SpringerLink](https://img.shields.io/badge/Springer-PDF-blue.svg)](https://rdcu.be/dkbIF)
[![Demo](https://img.shields.io/badge/Demo-Online-brightgreen.svg)](https://abdur75648-urduocr-utrnet.hf.space)

## Steps to run the code
***Note** - Due to several dependency issues in [maskrcnn-benchmark](https://github.com/facebookresearch/maskrcnn-benchmark), YoloV8 is used for text line detection. The model is finetuned on the [UrduDoc](https://paperswithcode.com/dataset/urdudoc) dataset.

* Clone the repository
* Install the dependencies
    ```bash
    pip install torch==2.0.1 ultralytics==8.1.8
    ```
* Put `test.jpg`
* Run `python3 detect.py`
* The output will be saved as `output.jpg`

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
