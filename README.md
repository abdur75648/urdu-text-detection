# Urdu OCR - Text Line Detection Inferencing

## Steps to run the code

* Clone the repository
* Download trained model (contourNet_model.pth) from [here](https://csciitd-my.sharepoint.com/:f:/g/personal/ch7190150_iitd_ac_in/EvLT451TYFpAmJglzzsISJYBzvlnbMeVn4lhnJg07xM4Qw?e=PbYDTJ)
* Run the following commands in the terminal
    * ```docker build -t ocr_docker .```
    * ```docker run -it --name ocr_app -v /Users/abdur/Desktop/cn_inference:/cn_inference ocr_docker```
    * ```cd cn_inference```
    * ```export INSTALL_DIR=$PWD```
    * ```cd $INSTALL_DIR && cd maskrcnn-benchmark && python3 setup.py build develop && cd $INSTALL_DIR```
    * ```unset INSTALL_DIR```
    * ```cp -r maskrcnn-benchmark/maskrcnn_benchmark .```

## License
Using this repository is not free for either commercial or non-commercial purposes. Please contact the authors for more details.