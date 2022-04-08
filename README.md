# Food Image Recognition and Calorie Estimation
Google Colab - 
https://colab.research.google.com/github/Arghya-Sengupta/Major-Project/blob/main/YOLOv5.ipynb

Download the Data from here - 
https://drive.google.com/drive/folders/169tjqFIs-gr1Ru6LXnuhInvYFi0Zhj4M?usp=sharing

Google Sheet for Training Accuracy - https://docs.google.com/spreadsheets/d/1_HPeNQ58W921psJhpR_WhonspteSroTeWoLdOJyyVaw/edit?usp=sharing

python D:/Project/yolov5/train.py --batch 2 --epochs 3 --data D:/Project/yolov5/data/custom_coco.yaml --weights yolov5s.pt --cache

python D:/Project/yolov5/custom_detect.py --weights D:/Project/yolov5/runs/train/exp........./weights/best.pt --conf 0.1 --source D:/Project/test.jpg

