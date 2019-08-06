import pandas as pd

d = pd.read_csv("E:/FYP/NewsOne/News-One.csv", encoding='ISO-8859-1')
e = pd.read_csv("E:/FYP/NewsOne/opinion.csv", encoding='ISO-8859-1')

f = pd.concat([d, e], axis=1)
f.to_csv("E:/FYP/NewsOne/Final-NewsOne.csv", index=False, encoding='utf-8')