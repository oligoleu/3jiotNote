### 2020/11/12
#### text detection
> 手寫辨識資料集 mnist emnist
* https://github.com/hunglc007/tensorflow-yolov4-tflite &emsp; object classification
* https://github.com/pythonlessons/TensorFlow-2.x-YOLOv3 &emsp; mnist
* https://github.com/penny4860/Yolo-digit-detector &emsp; text detection
* https://github.com/hsuRush/DeepANPR &emsp; license detection

#### yolo
* https://medium.com/@chih.sheng.huang821/深度學習-物件偵測yolov1-yolov2和yolov3-cfg-檔解讀-75793cd61a01
* https://mropengate.blogspot.com/2018/06/yolo-yolov3.html

### 2020/11/12
#### openssl batch generate crt
> https://gryzli.info/2015/03/05/openssl-usefull-commands/
```bash
# Runs in unattended batch mode
# Key length is                 : 2048 bits
# Certificate validity period   : 365 days
# [-nodes]                      : No password protection for the key
# New key file                  : self-ssl.key
# New certificate file          : self-ssl.crt

openssl req -batch  -nodes -newkey rsa:2048 -x509 -days 365 -keyout self-ssl.key -out self-ssl.crt
```
>https://www.jamescoyle.net/how-to/1073-bash-script-to-create-an-ssl-certificate-key-and-request-csr
