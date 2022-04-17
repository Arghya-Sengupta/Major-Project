# from calculate_calories import *

# total_calorie = get_foods()
# print("Total Calories = ",total_calorie)

import os

path = "D:/Project/"
detection_path = path +  "Detection_Images/"
results_path = path + "Results/"
N = len(os.listdir(detection_path))
os.mkdir(results_path)

for  i in range(1,N+1):
	test_file = "test" + str(i) +  ".jpg"
	command = "python /content/yolov5/detect.py --weights /content/yolov5/best.pt --conf 0.5 --source " + detection_path + test_file
	status = os.system(command)
	if(status != 0):
		print(test_file,"not found")