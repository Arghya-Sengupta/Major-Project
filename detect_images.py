import os
import time

path = "D:/Project/"
images_path = path +  "Testing_Images/"
results_path = path + "Results/"
weight_file = path + "/yolov5/runs/train/exp/weights/best.pt"
# N = len(os.listdir(images_path))
# start = time.time()

def detect_file(file_name):
	if not os.path.exists(results_path):
		os.mkdir(results_path)

	prog_path = path + "/yolov5/custom_detect.py"
	command = "python " + prog_path + " --weights " + weight_file + " --conf 0.3 --source " + file_name
	print("Detecting",file_name)

	try:
		status = os.system(command) # executing the command in cmd
	except Exception as e:
	    print("Error while Detecting")
	    print(e)
	if(status != 0):
		print("Error while Detecting")

# for test_file in os.listdir(images_path):
	# detect_file(images_path + file_name)

# print(f"Detection Completed in {round(time.time()-start, 2)}s")
