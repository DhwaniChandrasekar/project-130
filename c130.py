import csv
import pandas as pd

data = pd.read_csv("output129.csv")


data.drop(["Star_name.1","Distance.1","Mass.1","Radius.1","Luminosity","Unnamed: 6"], axis=1,inplace=True)

class130data = data.dropna()
print(class130data)

class130data.to_csv("c130output.csv")