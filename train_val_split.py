# code for spliting both images and labels for training and validation

import os
import shutil
from os.path import isfile, join
from random import randint
from os import listdir

directory = 'D:/Major-Project/Original_Images/'
nc = 5	# number of catagories

def make_directories():
	os.makedirs('D:/Major-Project/Training_Images/images/train')
	os.mkdir('D:/Major-Project/Training_Images/images/val')
	os.makedirs('D:/Major-Project/Training_Images/labels/train')
	os.mkdir('D:/Major-Project/Training_Images/labels/val')

def split_files(probability):
	make_directories()
	t=0
	v=0
	for i in range(1,nc+1):
		print("Working on "+str(i))
		new_dir = directory + str(i) + '/'
		for f in listdir(new_dir):
			if isfile(join(new_dir, f)) and f.endswith((".jpg", ".jpeg", ".png")):
				file_name = os.path.splitext(f)[0]
													
				if(randint(1, 100) <= probability):	
					split = 'train/'
					t +=1
				else:
					split = 'val/'
					v += 1

				imgage_src = new_dir + f
				imgage_dst = "D:/Major-Project/Training_Images/images/" + split

				label_src = directory + "labels/" + str(i) + "/" + file_name + ".txt"
				label_dst = "D:/Major-Project/Training_Images/labels/" + split

				shutil.copy2(imgage_src, imgage_dst)
				shutil.copy2(label_src, label_dst)
	print(str(t) + " (" + str(100.0*t/(t+v)) + " %) Images for training")
	print(str(v) + " (" + str(100.0*v/(t+v)) + " %) Images for validation")
	print('Completed\n\n')

# split_files(70) # 70% for training and 30% for validation