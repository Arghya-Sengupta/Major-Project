# delete the folder first (if present)
# %rm -rf /content/Training_Images
# code for spliting both images and labels for training and validation

import os
import glob
import shutil
from os.path import isfile, join
from random import randint
from os import listdir

directory = 'D:/Project/Original_Images/'
nc = 3	# number of catagories

def make_directories():
	os.makedirs('D:/Project/Training_Images/images/train')
	os.mkdir('D:/Project/Training_Images/images/val')
	os.makedirs('D:/Project/Training_Images/labels/train')
	os.mkdir('D:/Project/Training_Images/labels/val')

def split_files(probability):
	t=0
	v=0
	for i in range(1,nc+1):
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
				imgage_dst = "D:/Project/Training_Images/images/" + split

				label_src = directory + "labels/" + str(i) + "/" + file_name + ".txt"
				label_dst = "D:/Project/Training_Images/labels/" + split

				shutil.copy2(imgage_src, imgage_dst)
				shutil.copy2(label_src, label_dst)
	print(str(t) + " (" + str(100.0*t/(t+v)) + " %) Images for training")
	print(str(v) + " (" + str(100.0*v/(t+v)) + " %) Images for validation")

make_directories()
split_files(70)	# 70% for training and 30% for validation
