from tkinter import *
from PIL import Image
import os

from generate_yolo_bbox import create_labels
from train_val_split import split_files
from  detect_images import detect_file

root = Tk()
#root.geometry("675x500+120+120")
#root.minsize(675,395)
#root.maxsize(675,395)
canvas=Canvas(root,width=500,height=1000)
canvas.pack()
root.title("MAJOR PROJECT")

def train():
    command = "python D:/Project/yolov5/train.py --batch 2 --epochs 100 --data D:/Project/yolov5/data/custom_coco.yaml --weights yolov5s.pt"
    try:
        status = os.system(command) # executing the command in cmd
    except Exception as e:
        print("Error while Training")
        print(e)
    if(status != 0):
        print("Training stoped")

def show_result():
	im = Image.open(r"D:/Project/Results/result.jpg") 
	im.show()
	pass

b1=Button(root,text=" CREATE\nYOLO LABELS ",font=("BankGothic Md BT",12,"bold"),fg="aquamarine",padx=25,pady=18,relief=RAISED,bg="black",command=lambda:[create_labels()])
b1_placing=canvas.create_window(222,120,window=b1)

b2=Button(root,text=" CREATE\nTRAINING IMAGES ",font=("BankGothic Md BT",12,"bold"),fg="aquamarine",padx=10,pady=18,relief=RAISED,bg="black",command=lambda:[split_files(70)])
b2_placing=canvas.create_window(222,240,window=b2)

b3=Button(root,text=" TRAIN ",font=("BankGothic Md BT",12,"bold"),fg="red",padx=55,pady=28,relief=RAISED,bg="black",command=lambda:[train()])
b3_placing=canvas.create_window(222,360,window=b3)

file_name = "D:/Project/test.jpg"

b4=Button(root,text=" DETECT\nFROM IMAGE",font=("BankGothic Md BT",12,"bold"),fg="yellow",padx=33,pady=18,relief=RAISED,bg="black",command=lambda:[detect_file(file_name), show_result()])
b4_placing=canvas.create_window(222,480,window=b4)

b5=Button(root,text=" DETECT\nFROM CAMERA",font=("BankGothic Md BT",12,"bold"),fg="yellow",padx=22,pady=18,relief=RAISED,bg="black",command=lambda:[detect_file(file_name,0), show_result()])
b5_placing=canvas.create_window(222,600,window=b5)

if __name__ == '__main__':
    root.mainloop()
