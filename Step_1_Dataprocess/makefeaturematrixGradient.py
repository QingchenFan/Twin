
import scipy.io as scio
import glob
import pandas as pd
import numpy as np

label_files_all = pd.read_csv('/Users/qingchen/Documents/Data/Twin_2015_FC/label/label.csv')
label = label_files_all['id']
path = '/Users/qingchen/Documents/Data/Twin_2015_FC/gradient_alignment'
files_data = []
for i in label:
    print(i)
    i = str(i)
    alignmentpath = path + '/sub-' + i + '/'+'sub-'+i+'_gradient.mat'

    data = scio.loadmat(alignmentpath)

    temp = data['data']

    box = temp[:, 0:3]
    box = box.T
    res = np.array(box).flatten()
    files_data.append(res)
x_data = np.asarray(files_data)
print(x_data.shape)
np.savetxt('./schaefer400gradients.txt', x_data)