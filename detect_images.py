# detect 75 images

import os
import time

path = "/content/drive/MyDrive/Data/" # D:/Project
images_path = path +  "Detection_Images/"
results_path = path + "Results/"
N = len(os.listdir(images_path))
start = time.time()

if not os.path.exists(results_path):
	os.mkdir(results_path)

for test_file in os.listdir(images_path):
	prog_path = "/content/yolov5/custom_detect.py"
	weight_file = "/content/yolov5/runs/exp2/weights/best.pt"
	test_file = images_path + test_file

	command = "python " + prog_path + " --weights " + weight_file + " --conf 0.5 --source " + test_file
	print("Detecting",test_file)

	try:
		status = os.system(command) # executing the command in cmd
	except Exception as e:
	    print("Error while executing custom_detect.py")
	    print(e)

	if(status != 0):
		print(test_file,"not found")

print(f"Detection Completed in {round(time.time()-start, 2)}s")
