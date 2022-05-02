from tkinter import *
from PIL import Image,ImageTk
import os

from generate_yolo_bbox import create_labels
from train_val_split import split_files
from  detect_images import detect_file

root = Tk()
#root.geometry("675x500+120+120")
#root.minsize(675,395)
#root.maxsize(675,395)
canvas=Canvas(root,width=1000,height=1000)
canvas.pack()
root.title("CALORIE FINDER")

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

b1=Button(root,text=" CREATE\nYOLO LABELS ",font=("BankGothic Md BT",12,"bold"),fg="aquamarine",pady=5,padx=5,relief=RAISED,bg="black",command=lambda:[create_labels()])
b1_placing=canvas.create_window(222,120,window=b1)

b2=Button(root,text=" CREATE\nTRAINING IMAGES ",font=("BankGothic Md BT",12,"bold"),fg="aquamarine",padx=26,pady=18,relief=RAISED,bg="black",command=lambda:[split_files(70)])
b2_placing=canvas.create_window(450,120,window=b2)

b3=Button(root,text=" TRAIN ",font=("BankGothic Md BT",12,"bold"),fg="yellow",pady=20,padx=4,relief=RAISED,bg="black",command=lambda:[train()])
b3_placing=canvas.create_window(452,250,window=b3)

file_name = "D:/Project/test.jpg"
b4=Button(root,text=" DETECT ",font=("BankGothic Md BT",12,"bold"),fg="yellow",padx=31,pady=3,relief=RAISED,bg="black",command=lambda:[detect_file(file_name), show_result()])
b4_placing=canvas.create_window(220,250,window=b4)

if __name__ == '__main__':
    root.mainloop()
