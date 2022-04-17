# Estimating Food Calories for Multiple-dish Food Photos using YOLOv5
YOLO (You Only Look Once) is an object detection algorithm that divides images into a grid system. Each cell in the grid is responsible for detecting objects within itself. YOLO is one of the most famous object detection algorithms due to its speed and accuracy. [Glenn Jocher](https://www.linkedin.com/in/glenn-jocher) introduced YOLOv5 using the Pytorch framework. We have referred to the [YOLOv5 documentation](https://docs.ultralytics.com) for training and testing. Other resources can be found below:-

- [Google Colab](https://colab.research.google.com/github/Arghya-Sengupta/Major-Project/blob/main/YOLOv5.ipynb)

- [Original Dataset](http://foodcam.mobi/dataset100.html)

- [Reference Research Paper](https://drive.google.com/file/d/1jsvMc41_EPGKejEG-NMBzA6Ll6HqRhKa/view?usp=sharing)

- [Google Sheet](https://docs.google.com/spreadsheets/d/1_HPeNQ58W921psJhpR_WhonspteSroTeWoLdOJyyVaw/edit?usp=sharing) for Training Accuracy

- [Zenodo](https://zenodo.org/record/6222936#.YlaVKfpBzIU)

- **Paste the above codes under _`D:/Project/`_**
   > Download the **`Training_Images`** folder from [here](https://drive.google.com/drive/folders/169tjqFIs-gr1Ru6LXnuhInvYFi0Zhj4M?usp=sharing "Google Drive").
   > 
   > Clone the YOLOv5 repo `git clone https://github.com/ultralytics/yolov5`

- **For Training run the following code**
   > *python D:/Project/yolov5/train.py --batch 2 --epochs 1 --data D:/Project/yolov5/data/custom_coco.yaml --weights yolov5s.pt --cache*

- **For Detection run the following code**
   > *python D:/Project/yolov5/custom_detect.py --weights D:/Project/yolov5/runs/train/exp........./weights/best.pt --conf 0.1 --source D:/Project/test.jpg*

## Folder Structure
![Folder Structure](https://github.com/Arghya-Sengupta/Major-Project/blob/main/Folder%20Structure.jpg "Made using Lucidchart")
