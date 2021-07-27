import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])


data_dict = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}
squirrel_count = pd.DataFrame(data_dict)
squirrel_count.to_csv("squirrel_count.csv")
