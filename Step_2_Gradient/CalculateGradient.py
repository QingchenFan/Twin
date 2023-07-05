import glob
import os
import nibabel as nib
from brainspace.gradient import GradientMaps
from brainspace.datasets import load_group_fc, load_parcellation, load_conte69
from scipy.io import savemat
import numpy as np

path = '/Users/qingchen/Documents/Data/Twin_2015_FC/FC/'
filename = os.listdir(path)
#filename = ['sub-0032']
FClist = []
for i in filename:
    #print(i)
    file = path + i
    data = glob.glob(file + '/*.nii')
    m = nib.load(data[0]).get_fdata()
    FClist.append(m)
    # Ask for 10 gradients (default)
    # gm = GradientMaps(kernel='normalized_angle', n_components=10, random_state=0)
    # resgm = gm.fit(m)
    #
    # resdata = resgm.gradients_
    # newpath = '/Users/qingchen/Documents/Data/Twin_2015_FC/gradient/'+ i
    # if not os.path.exists(newpath):
    #     os.makedirs(newpath)
    # savemat('/Users/qingchen/Documents/Data/Twin_2015_FC/gradient/'+i+'/'+i+'_gradient.mat', {'data': resdata})

gp = GradientMaps(kernel='normalized_angle', alignment='procrustes', n_components=10, random_state=0)
gp.fit(FClist)

res = gp.gradients_

for g in res:
    newpath = '/Users/qingchen/Documents/Data/Twin_2015_FC/gradient_alignment/'+ i
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    savemat('/Users/qingchen/Documents/Data/Twin_2015_FC/gradient_alignment/'+i+'/'+i+'_gradient.mat', {'data': g})