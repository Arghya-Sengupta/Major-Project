# fetch food calorie from https://www.fatsecret.com/calories-nutrition/search?q=

import requests
from bs4 import BeautifulSoup

url = 'https://www.fatsecret.com/calories-nutrition/search?q='

def search_in_text(arr, text):
    for i in range(0,len(arr)):
        if(arr[i].lower().strip() == text.lower().strip()):
            return i
    return -1

def fetch_calories(food_name):
    try:
        s = url + food_name
        req = requests.get(s).text
        scrap = BeautifulSoup(req, 'html.parser')

        class_name = "smallText greyText greyLink"
        text = scrap.find("div", class_=class_name).text
        arr = text.split(" ")
        i = search_in_text(arr,"Calories:")
        return arr[i+1]

    except Exception as e:
        print(f"Unable to fetch the Calories of {food_name}")
        print(e)


# Testing

# foods = ['rice','toast','omelet','fish','salad','banana']
# for food_name in foods:
#     calories = fetch_calories(food_name)
#     print(food_name + " has " + calories)


# s = url + 'omelet'
# req = requests.get(s).text
# # print(req)

# scrap = BeautifulSoup(req, 'html.parser')
# text = scrap.find("div", class_="smallText greyText greyLink").text
# arr = text.split(" ")
# i = search(arr,"Calories:")
# print(arr[i+1])