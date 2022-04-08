# Food Image Recognition and Calorie Estimation
[Google Colab](https://colab.research.google.com/github/Arghya-Sengupta/Major-Project/blob/main/YOLOv5.ipynb)

[Original Dataset](http://foodcam.mobi/dataset100.html)

[YOLOv5 Documentation](https://docs.ultralytics.com/)

[Reference Research Paper](https://drive.google.com/file/d/1jsvMc41_EPGKejEG-NMBzA6Ll6HqRhKa/view?usp=sharing)

[Google Sheet](https://docs.google.com/spreadsheets/d/1_HPeNQ58W921psJhpR_WhonspteSroTeWoLdOJyyVaw/edit?usp=sharing) for Training Accuracy

**Download the folders colored _GREEN_**
> https://drive.google.com/drive/folders/169tjqFIs-gr1Ru6LXnuhInvYFi0Zhj4M?usp=sharing
> 
> Paste these under ***D:/Project/***

**For Training**
> *python D:/Project/yolov5/train.py --batch 2 --epochs 1 --data D:/Project/yolov5/data/custom_coco.yaml --weights yolov5s.pt --cache*

**For Detection**
> *python D:/Project/yolov5/custom_detect.py --weights D:/Project/yolov5/runs/train/exp........./weights/best.pt --conf 0.1 --source D:/Project/test.jpg*
