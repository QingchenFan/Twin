import pandas as pd
import os

imagepath = '/Users/qingchen/Documents/Data/Twin_2015_FC/gradient_alignment'
filename = os.listdir(imagepath)
labelpath = '/Users/qingchen/Documents/Data/Twin_2015_FC/label/label.csv'
label = pd.read_csv(labelpath)
id = label['id'].tolist()
print(type(id[0]))
aa = []
for i in filename:

    a = int(i[4:])

    if a not in id:
        aa.append(a)
print(aa)
# for i in id:
#     a = 'sub-'+str(i)
#     if a not in filename:
#         print(a)
# for j in aa:
#     cmd = 'rm -rf '+imagepath+'/sub-'+str(j)
#     os.system(cmd)