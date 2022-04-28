# fetch food calorie from https://www.myfitnesspal.com/food/search

import requests
from bs4 import BeautifulSoup

url = 'https://www.myfitnesspal.com/food/search?page=1&search='

def fetch_calories(food_name):
    try:
        search = url + food_name
        req = requests.get(search).text
        scrap = BeautifulSoup(req, 'html.parser')

        class_name = "label-1frn-"
        calories = scrap.find("div", class_=class_name).text

        return calories

    except Exception as e:
        print(f"Unable to fetch the Calories of {food_name}")
        print(e)


# Testing

# foods = ['rice','toast','16443543','omelet','fish','salad','banana']
# for food_name in foods:
#     calories = fetch_calories(food_name)
#     if((calories is not None) and calories.isnumeric()):
#         print(f"{food_name} has {calories} kcal per 100gm")


# url = 'https://www.myfitnesspal.com/food/search?page=1&search=' + 'rice'
# req = requests.get(url).text
# print(req)

# scrap = BeautifulSoup(req, 'html.parser')
# calories = scrap.find("div", class_="label-1frn-").text
# print(calories)