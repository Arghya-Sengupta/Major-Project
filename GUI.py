from tkinter import *
from PIL import Image
import os

from generate_yolo_bbox import create_labels
from train_val_split import split_files
from  detect_images import detect_file

root = Tk()
canvas=Canvas(root,width=500,height=1000)
canvas.pack()
root.title("Food Item Detection and Calorie Estimation using YOLOv5")

def train():
    command = "python D:/Major-Project/yolov5/train.py --batch 2 --epochs 100 --data D:/Major-Project/yolov5/data/custom_coco.yaml --weights yolov5s.pt"
    try:
        status = os.system(command) # executing the command in cmd
    except Exception as e:
        print("Error while Training")
        print(e)
    if(status != 0):
        print("Training stoped")

def show_result():
    im = Image.open(r"D:/Major-Project/Results/result.jpg") 
    im.show()
    pass

b1=Button(root,text=" CREATE\nYOLO LABELS ",font=("BankGothic Md BT",12,"bold"),fg="aquamarine",padx=25,pady=18,relief=RAISED,bg="black",command=lambda:[create_labels()])
b1_placing=canvas.create_window(222,120,window=b1)

b2=Button(root,text=" CREATE\nTRAINING IMAGES ",font=("BankGothic Md BT",12,"bold"),fg="aquamarine",padx=10,pady=18,relief=RAISED,bg="black",command=lambda:[split_files(70)])
b2_placing=canvas.create_window(222,240,window=b2)

b3=Button(root,text=" TRAIN ",font=("BankGothic Md BT",12,"bold"),fg="yellow",padx=55,pady=28,relief=RAISED,bg="black",command=lambda:[train()])
b3_placing=canvas.create_window(222,360,window=b3)

file_name = "D:/Major-Project/test.jpg"
b4=Button(root,text=" DETECT ",font=("BankGothic Md BT",12,"bold"),fg="yellow",padx=47,pady=28,relief=RAISED,bg="black",command=lambda:[detect_file(file_name), show_result()])
b4_placing=canvas.create_window(222,480,window=b4)

if __name__ == '__main__':
    root.mainloop()