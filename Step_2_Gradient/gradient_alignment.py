import glob
import os
import nibabel as nib
from brainspace.gradient import GradientMaps
from brainspace.datasets import load_group_fc, load_parcellation, load_conte69
from scipy.io import savemat
import numpy as np

path = '/Users/qingchen/Documents/Data/Twin_2015_FC/FC/'
filename = os.listdir(path)
FClist = []
print(filename)
for i in filename:
    print(i)
    file = path + i
    data = glob.glob(file + '/*.nii')
    m = nib.load(data[0]).get_fdata()
    FClist.append(m)

gp = GradientMaps(kernel='normalized_angle', alignment='procrustes', n_components=10, random_state=0)
gp.fit(FClist)
res = gp.gradients_

for j, g in zip(filename, res):
    print('j--', j)
    newpath = '/Users/qingchen/Documents/Data/Twin_2015_FC/gradient_alignment/'+ j
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    savemat('/Users/qingchen/Documents/Data/Twin_2015_FC/gradient_alignment/'+j+'/'+j+'_gradient.mat', {'data':g})