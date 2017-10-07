# Meta Detection

## Models
* RRC
  * https://github.com/xiaohaoChen/rrc_detection
  * https://drive.google.com/open?id=0ByGD7RFf_dTxS2ZWcWo5cTVQaDQ
* SSD
  * https://github.com/weiliu89/caffe/tree/ssd
  * https://drive.google.com/open?id=0BzKzrI_SkD1_NVVNdWdYNEh1WTA

## Dataset
* Udacity
  * https://github.com/udacity/self-driving-car/tree/master/annotations#dataset-2

## Evaluation
Detection results are evaluated using [script](https://github.com/getnexar/challenge2-evaluation/tree/61474959ac959446feae808a15b5ca5836a0aca3) from Nexar.

### Conversion UDACITY to NEXAR format
```bash
udacity2nexar.py -i udacity/labels_car.csv -o udacity_nexar_format.csv
```

### Conversion KITTI to NEXAR format
```bash
./kitti2nexar.py -i ssd/ -o ssd_nexar_format.csv
./kitti2nexar.py -i rrc/ -o rrc_nexar_format.csv
```

### SSD Evaluation
AP 0.2315249589110112

### RRC Evaluation
AP 0.20620831108034546
