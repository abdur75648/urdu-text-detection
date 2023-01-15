# Urdu OCR - Text Line Detection Inferencing

## Steps to run the code
* docker build -t ocr_docker .
* docker run -it --name ocr_app -v /Users/abdur/Desktop/cn_inference:/cn_inference ocr_docker
* cd cn_inference
* export INSTALL_DIR=$PWD
* cd $INSTALL_DIR && git clone https://github.com/NVIDIA/apex && cd apex/ && python3 setup.py install
* cd $INSTALL_DIR && cd maskrcnn-benchmark && python3 setup.py build develop && cd $INSTALL_DIR
* unset INSTALL_DIR
* cp -r maskrcnn-benchmark/maskrcnn_benchmark .