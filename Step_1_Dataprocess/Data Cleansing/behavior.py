import os
import pandas as pd
import numpy as np
imagepath = '/Users/qingchen/Documents/Data/Twin_2015_FC/FC'
filename = os.listdir(imagepath)

bev = pd.read_csv('/Users/qingchen/Documents/Data/Twin_2015_FC/label/twin2015all.csv')

 # 返回的是array([0, 2, 4, 6, 7])

l = []
data = []

# 创建DataFrame


for i in filename:

    newname = int(i[4:])
    print(newname)
    # index = bev[bev["id"] == newname].index.tolist()[0]
    # a = bev.iloc[index:index+1, :]
    # print(a)
    #  获取某一行
    if newname in list(bev['id']):
        mask = bev['id'] == newname
        pos = np.flatnonzero(mask)
        a = bev.iloc[pos].values.tolist()  # 根据列值获取一行

        l.append(str(a))

        #pd.concat([df, a], axis=0)
print(len(l))

fw = open("./label.csv", mode='w')

for j in l:
    fw.write('\n')
    print(j)
    fw.write(j)


