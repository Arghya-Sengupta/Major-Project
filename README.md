# Food Image Recognition and Calorie Estimation
Google Colab - 
https://colab.research.google.com/github/Arghya-Sengupta/Major-Project/blob/main/YOLOv5.ipynb

Download the Dateset from here - 
https://drive.google.com/drive/folders/169tjqFIs-gr1Ru6LXnuhInvYFi0Zhj4M?usp=sharing

For training the model - 
python D:/Project/yolov5/train.py --img 240 --batch 2 --epochs 3 --data D:/Project/yolov5/data/custom_coco.yaml --weights yolov5s.pt --cache

For detecting an image - 
python D:/Project/yolov5/detect.py --weights D:/Project/yolov5/runs/train/exp12/weights/best.pt --img 640 --conf 0.1 --source D:/Project/test.jpg
