from tkinter import *
from PIL import Image,ImageTk
import os

from generate_yolo_bbox import create_labels
from train_val_split import split_files
from  detect_images import detect_file

root = Tk()
root.geometry("675x500+120+120")
root.minsize(675,395)
root.maxsize(675,395)
# rootwalpaper=Image.open("rootwallpaper.jpg")
# bgimg=ImageTk.PhotoImage(rootwalpaper)
canvas=Canvas(root,width=675,height=500)
canvas.pack()
# canvas.create_image(335,195,image=bgimg)
root.title("CALORIE FINDER")
# root.iconbitmap("icon.ico")

def train():
    command = "python D:/Project/yolov5/train.py --batch 2 --epochs 100 --data D:/Project/yolov5/data/custom_coco.yaml --weights yolov5s.pt"
    try:
        status = os.system(command) # executing the command in cmd
    except Exception as e:
        print("Error while executing train.py")
        print(e)
    if(status != 0):
        print("train.py not found")

def show_image():
	im = Image.open(r"D:/Project/Result/result.jpg") 
	im.show()
	pass

b1=Button(root,text=" CREATE\nYOLO LABELS ",font=("BankGothic Md BT",12,"bold"),fg="aquamarine",pady=5,padx=5,relief=RAISED,bg="black",command=lambda:[create_labels()])
b1_placing=canvas.create_window(222,120,window=b1)

b2=Button(root,text=" CREATE\nTRAINING IMAGES ",font=("BankGothic Md BT",12,"bold"),fg="aquamarine",padx=26,pady=18,relief=RAISED,bg="black",command=lambda:[split_files(70)])
b2_placing=canvas.create_window(450,120,window=b2)

b3=Button(root,text=" TRAIN ",font=("BankGothic Md BT",12,"bold"),fg="yellow",pady=20,padx=4,relief=RAISED,bg="black",command=lambda:[train()])
b3_placing=canvas.create_window(452,250,window=b3)

entry= Entry(root, text="Enter a file name from D:/Testing_Images", width=100)
entry.focus_set()
entry.pack()
file_name = entry.get()

b4=Button(root,text=" DETECT ",font=("BankGothic Md BT",12,"bold"),fg="yellow",padx=31,pady=3,relief=RAISED,bg="black",command=lambda:[detect_file(file_name), show_image()])
b4_placing=canvas.create_window(220,250,window=b4)

if __name__ == '__main__':
    root.mainloop()