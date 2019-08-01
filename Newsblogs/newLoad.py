import pandas as pd
import csv

# pathold = 'E:\webapplications (2)\webapplications\\dunya.csv'
pathDunya= 'C:\\Users\\Zain Noman\\PycharmProjects\\webapplications(4-4-19)\\webapplications\\Final-Dunya.csv'
pathAry = 'C:\\Users\\Zain Noman\\PycharmProjects\\webapplications(4-4-19)\\webapplications\\Final-ARY.csv'
pathNOne = 'C:\\Users\\Zain Noman\\PycharmProjects\\webapplications(4-4-19)\\webapplications\\Final-NewsOne.csv'
chunk_size = 500

# readold=pd.read_csv(pathold, iterator = True)
# df1=readold.get_chunk(chunk_size)

readDunya=pd.read_csv(pathDunya, iterator = True)
dfD=readDunya.get_chunk(chunk_size)
# print(dfD)
readAry=pd.read_csv(pathAry, iterator = True)
dfA=readAry.get_chunk(chunk_size)
# print(df['title'], df['img-url'], df['summerize-news'])
# for index, row in dfA.iterrows():
#     dt2=index, row['title'], row['img-url'], row['category'],row['sumery_Ary']
#     print(dt2[4])

readNOne=pd.read_csv(pathNOne, iterator = True)
dfN=readNOne.get_chunk(chunk_size)
# for index, row in dfN.iterrows():
#     dt2=index, row['title'], row['img-url'], row['category'],row['sum-NO']
#     print(dt2[4])