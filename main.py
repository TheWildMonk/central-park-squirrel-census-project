import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = data["Primary Fur Color"].to_list()

gray = 0
red = 0
black = 0
for each_color in fur_color:
    if each_color == "Gray":
        gray += 1
    elif each_color == "Cinnamon":
        red += 1
    elif each_color == "Black":
        black += 1

data_dict = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [gray, red, black]
}
squirrel_count = pd.DataFrame(data_dict)
squirrel_count.to_csv("squirrel_count.csv")
