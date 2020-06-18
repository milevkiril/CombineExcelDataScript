import pandas as pd
import numpy as np
import os, collections, csv
from os.path import basename

df = []
f = "C:\\Users\\Admin\\Desktop\\Email_data\\Users_email.xlsx"
numberOfSheets = 18

for i in range(1,numberOfSheets+1):
    data = pd.read_excel(f, sheetname = 'Part ' +str(i), header=None)
    df.append(data)
final = "C:\\Users\\Admin\\Desktop\\Email_data\\Combined.csv"
df = pd.concat(df)
df.to_csv(final)

print("done")