import nibabel as nib
import os
import glob
# path = '/Users/qingchen/Documents/Data/Twin_2015_FC/FC/'
# from scipy.io import savemat
# filename = os.listdir(path)
# for i in filename:
#     print(i)
#     file = path + i
#     data = glob.glob(file + '/*.nii')
#     m = nib.load(data[0]).get_fdata()
#
#     newpath = '/Users/qingchen/Documents/Data/Twin_2015_FC/gradient_m/' + i
#     if not os.path.exists(newpath):
#         os.makedirs(newpath)
#     savemat('/Users/qingchen/Documents/Data/Twin_2015_FC/gradient_m/' + i + '/func_gordonsubcortical.mat', {'data': m})
from brainspace.datasets import load_group_fc, load_parcellation, load_conte69

# First load mean connectivity matrix and Schaefer parcellation
conn_matrix = load_group_fc('schaefer', scale=400)
labeling = load_parcellation('schaefer', scale=400, join=True)   # labeling 64984
print('labeling-', labeling.shape)
# and load the conte69 surfaces
surf_lh, surf_rh = load_conte69()
print('surf_lh-', surf_lh)
print('surf_rh-', surf_rh)


from brainspace.plotting import plot_hemispheres

# plot_hemispheres(surf_lh, surf_rh, array_name=labeling, size=(1200, 200),
#                  cmap='tab20', zoom=1.85)

from brainspace.gradient import GradientMaps

# Ask for 10 gradients (default)
gm = GradientMaps(n_components=10, random_state=0)
gm.fit(conn_matrix)

import numpy as np

from brainspace.utils.parcellation import map_to_labels

mask = labeling != 0

grad = [None] * 2

for i in range(2):
    # map the gradient to the parcels
    grad[i] = map_to_labels(gm.gradients_[:, i], labeling, mask=mask, fill=np.nan)
print(grad[1].shape)

plot_hemispheres(surf_lh, surf_rh, array_name=grad, size=(1200, 400), cmap='viridis_r',
                 color_bar=True, label_text=['Grad1', 'Grad2'], zoom=1.55)