import os

imagepath = '/Users/qingchen/Documents/Data/Twin_2015_FC/FC_mat'
filename = os.listdir(imagepath)

for i in filename:
    print(i)
    newname = 'sub-9' + i[4:7] + '0' + i[-1]
    print(newname)
    oname = imagepath + '/' + i
    nname = imagepath + '/' + newname
    os.rename(oname, nname)
