# Food Item Detection and Calorie Estimation using YOLOv5
YOLO (You Only Look Once) is an object detection algorithm that divides images into a grid system. Each cell in the grid is responsible for detecting objects within itself. YOLO is one of the most famous object detection algorithms due to its speed and accuracy. [Glenn Jocher](https://www.linkedin.com/in/glenn-jocher) introduced YOLOv5 using the Pytorch framework. We have referred to the [YOLOv5 documentation](https://docs.ultralytics.com) for training and testing. Other resources can be found below:-

- [Google Colab](https://colab.research.google.com/github/Arghya-Sengupta/Project/blob/main/YOLOv5.ipynb#scrollTo=HqHDViXe4u6s)

- [Original Dataset](http://foodcam.mobi/dataset100.html)

- [Project Documentation](https://drive.google.com/file/d/1ecb3buVpqab_AudhyEdYZSaHI1hZfJ81/view?usp=sharing)

- [Reference Research Paper](https://drive.google.com/file/d/1jsvMc41_EPGKejEG-NMBzA6Ll6HqRhKa/view?usp=sharing)

- **Steps to execute the code:**
   > Open cmd and run the bellow commands:
   > ```
   > d:
   > git clone https://github.com/Arghya-Sengupta/Project
   > cd Project
   > cd yolov5
   > git init
   > git remote add origin https://github.com/ultralytics/yolov5
   > git fetch
   > git checkout origin/master -ft
   > git pull
   > 
   > ```
   > Download the _`Original_Images`_ folder from [Google Drive](https://drive.google.com/drive/folders/169tjqFIs-gr1Ru6LXnuhInvYFi0Zhj4M?usp=sharing "Google Drive").

- **For detecting using camera:**
   > Open cmd and run the bellow commands:
   > ```
   > d:
   > python D:/Project/yolov5/custom_detect.py --weights D:/Project/yolov5/runs/train/exp/weights/best.pt --conf 0.3 --source 0
   > 
   > ```

## Flowchart
![Flowchart](https://github.com/Arghya-Sengupta/Major-Project/blob/main/Flowchart.png "Flowchart")
