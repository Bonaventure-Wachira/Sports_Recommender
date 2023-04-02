import pandas as pd
import numpy as np

attributes = [
    "Endurance", "Strength", 
    "Power", "Speed", 
    "Agility", "Flexibility", 
    "Nerve", "Durability", 
    "Hand-Eye Coordination", "Analytical Aptitude"
]

def recommend_sport(inputs):
    df = pd.read_excel("Toughest Sport by Skill.xlsx")
    attr_table = df[attributes]
    user = pd.DataFrame(inputs, index=[0], columns=attributes)
    tmp = attr_table.to_numpy() - user.to_numpy()
    mse = np.square(tmp).sum(axis=1)
    sportRes = {"Sport":df["Sport"].values, "MSE":mse}
    sportMetrics = pd.DataFrame(sportRes, columns=["Sport", "MSE"])
    inx = sportMetrics["MSE"].idxmin()
    return sportMetrics['Sport'][inx]


