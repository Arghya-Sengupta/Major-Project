# delete the UECFOOD100 folder first (if present)
# %rm -rf /content/UECFOOD100
# code for spliting both images and labels for training and validation

import os
import glob
import shutil
from os.path import isfile, join
from random import randint
from os import listdir

directory = '/content/sample_data/'
nc = 3	# number of catagories

def make_directories():
	os.makedirs('/content/UECFOOD100/images/train')
	os.mkdir('/content/UECFOOD100/images/val')
	os.makedirs('/content/UECFOOD100/labels/train')
	os.mkdir('/content/UECFOOD100/labels/val')

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
				imgage_dst = "/content/UECFOOD100/images/" + split

				label_src = directory + "labels/" + str(i) + "/" + file_name + ".txt"
				label_dst = "/content/UECFOOD100/labels/" + split

				shutil.copy2(imgage_src, imgage_dst)
				shutil.copy2(label_src, label_dst)
	print(t,"Images for training")
	print(v,"Images for validation")

make_directories()
split_files(70)	# 70% for training and 30% for validation
