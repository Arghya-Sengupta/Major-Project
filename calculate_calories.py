import pandas as pd

calorie_file = pd.read_csv('D:/Project/Calorie_Data.csv')
result_file = 'D:/Project/result.txt'

def search(food):
	i = 0
	for food_name in calorie_file.Food_Name:
		if(food.lower() == food_name.lower()):
			return i
		i += 1
	return 0

def get_foods():
	total = 0
	with open(result_file) as result:
		for food in result:
			food = food.strip()
			if(food is ''):
				continue
			calorie = calorie_file.Calories[search(food)]
			total += calorie
	return total

total_calorie = 0
total_calorie = get_foods()
print("Total Calories = ",total_calorie)