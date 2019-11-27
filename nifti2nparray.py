#!/usr/bin/env python3

'''
@author: d. lussier
downloads  resting-state fmri data, randomizes and splits into train and test sets, and organizes data by site into label folders
extracts timeseries correlations and saves as a numpy array file for later conversion to graph
'''

import os
import re
import shutil
import time
import numpy as np
from nilearn import datasets
from glob import glob
from tqdm import tqdm
from shutil import copyfile
from sklearn.model_selection import train_test_split
from nilearn.input_data import NiftiMapsMasker
from nilearn.connectome import ConnectivityMeasure

#import atlas
atlas = datasets.fetch_harvard_oxford()
# Loading atlas image stored in 'maps'
atlas_filename = atlas['maps']
# Loading atlas data stored in 'labels'
labels = atlas['labels']

#import dataset in increments to avoid being disconnected from the server
data = datasets.fetch_abide_pcp(data_dir='./data/', pipeline='niak', derivatives=['func_preproc','rois_ho'], SITE_ID=['PITT'], n_subjects=500)
time.sleep(60)
data = datasets.fetch_abide_pcp(data_dir='./data/', pipeline='niak', derivatives=['func_preproc','rois_ho'], SITE_ID=['OLIN'], n_subjects=500)
time.sleep(60)
data = datasets.fetch_abide_pcp(data_dir='./data/', pipeline='niak', derivatives=['func_preproc','rois_ho'], SITE_ID=['OHSU'], n_subjects=500)
time.sleep(60)
data = datasets.fetch_abide_pcp(data_dir='./data/', pipeline='niak', derivatives=['func_preproc','rois_ho'], SITE_ID=['SDSU'], n_subjects=500)
time.sleep(60)
data = datasets.fetch_abide_pcp(data_dir='./data/', pipeline='niak', derivatives=['func_preproc','rois_ho'], SITE_ID=['UM_1'], n_subjects=500)
time.sleep(60)
data = datasets.fetch_abide_pcp(data_dir='./data/', pipeline='niak', derivatives=['func_preproc','rois_ho'], SITE_ID=['UM_2'], n_subjects=500)
time.sleep(60)
data = datasets.fetch_abide_pcp(data_dir='./data/', pipeline='niak', derivatives=['func_preproc','rois_ho'], SITE_ID=['USM'], n_subjects=500)
time.sleep(60)
data = datasets.fetch_abide_pcp(data_dir='./data/', pipeline='niak', derivatives=['func_preproc','rois_ho'], SITE_ID=['YALE'], n_subjects=500)
time.sleep(60)
data = datasets.fetch_abide_pcp(data_dir='./data/', pipeline='niak', derivatives=['func_preproc','rois_ho'], SITE_ID=['CMU'], n_subjects=500)
time.sleep(60)
data = datasets.fetch_abide_pcp(data_dir='./data/', pipeline='niak', derivatives=['func_preproc','rois_ho'], SITE_ID=['LEUVEN_1'], n_subjects=500)
time.sleep(60)
data = datasets.fetch_abide_pcp(data_dir='./data/', pipeline='niak', derivatives=['func_preproc','rois_ho'], SITE_ID=['LEUVEN_2'], n_subjects=500)
time.sleep(60)
data = datasets.fetch_abide_pcp(data_dir='./data/', pipeline='niak', derivatives=['func_preproc','rois_ho'], SITE_ID=['KKI'], n_subjects=500)
time.sleep(60)
data = datasets.fetch_abide_pcp(data_dir='./data/', pipeline='niak', derivatives=['func_preproc','rois_ho'], SITE_ID=['NYU'], n_subjects=500)
time.sleep(60)
data = datasets.fetch_abide_pcp(data_dir='./data/', pipeline='niak', derivatives=['func_preproc','rois_ho'], SITE_ID=['STANFORD'], n_subjects=500)
time.sleep(60)
data = datasets.fetch_abide_pcp(data_dir='./data/', pipeline='niak', derivatives=['func_preproc','rois_ho'], SITE_ID=['TRINITY'], n_subjects=500)
time.sleep(60)
data = datasets.fetch_abide_pcp(data_dir='./data/', pipeline='niak', derivatives=['func_preproc','rois_ho'], SITE_ID=['UCLA_1'], n_subjects=500)
time.sleep(60)
data = datasets.fetch_abide_pcp(data_dir='./data/', pipeline='niak', derivatives=['func_preproc','rois_ho'], SITE_ID=['UCLA_2'], n_subjects=500)
time.sleep(60)
data = datasets.fetch_abide_pcp(data_dir='./data/', pipeline='niak', derivatives=['func_preproc','rois_ho'], SITE_ID=['MAX_MUN'], n_subjects=500)
time.sleep(60)
data = datasets.fetch_abide_pcp(data_dir='./data/', pipeline='niak', derivatives=['func_preproc','rois_ho'], SITE_ID=['CALTECH'], n_subjects=500)
time.sleep(60)
data = datasets.fetch_abide_pcp(data_dir='./data/', pipeline='niak', derivatives=['func_preproc','rois_ho'], SITE_ID=['SBL'], n_subjects=500)

func = data.func_preproc #4D data

# print basic information on the dataset
print('First functional nifti image (4D) is at: %s' % #location of image
      func[0])  
print(data.keys())

#create needed directories
func_dir = os.path.dirname(os.path.realpath(func[0]))
phenotype = os.path.join(func_dir, '../../ABIDE_pcp/Phenotypic_V1_0b_preprocessed1.csv')

train_dir = './data/train/'
test_dir = './data/test/'
for p in [train_dir,test_dir]:
    if not os.path.exists(p):
        os.mkdir(p)

#randomize and split training and test data 
all_files = glob(os.path.join(func_dir,"*.nii.gz"))

train,test = train_test_split(all_files,test_size = 0.2,random_state = 12345, shuffle=True)

for t in tqdm(train):
    copyfile(t,os.path.join(train_dir,os.path.split(t)[1]))
    
for t in tqdm(test):
    copyfile(t,os.path.join(test_dir,os.path.split(t)[1]))

#move data into respective site id label folders
pitt_dir = './data/train/pitt/'
olin_dir = './data/train/olin/'
ohsu_dir = './data/train/ohsu/'
sdsu_dir = './data/train/sdsu/'
trinity_dir = './data/train/trinity/'
um_1_dir = './data/train/um_1/'
um_2_dir = './data/train/um_2/'
usm_dir = './data/train/usm/'
yale_dir = './data/train/yale/'
cmu_dir = './data/train/cmu/'
leuven_1_dir = './data/train/leuven_1/'
leuven_2_dir = './data/train/leuven_2/'
kki_dir = './data/train/kki/'
nyu_dir = './data/train/nyu/'
stanford_dir = './data/train/stanford'
ucla_1_dir = './data/train/ucla_1/'
ucla_2_dir = './data/train/ucla_2/'
maxmun_dir = './data/train/maxmun/'
caltech_dir = './data/train/caltech/'
sbl_dir = './data/train/sbl/'
pitt_test_dir = './data/test/pitt/'
olin_test_dir = './data/test/olin/'
ohsu_test_dir = './data/test/ohsu/'
sdsu_test_dir = './data/test/sdsu/'
trinity_test_dir = './data/test/trinity/'
um_1_test_dir = './data/test/um_1/'
um_2_test_dir = './data/test/um_2/'
usm_test_dir = './data/test/usm/'
yale_test_dir = './data/test/yale/'
cmu_test_dir = './data/test/cmu/'
leuven_1_test_dir = './data/test/leuven_1/'
leuven_2_test_dir = './data/test/leuven_2/'
kki_test_dir = './data/test/kki/'
nyu_test_dir = './data/test/nyu/'
stanford_test_dir = './data/test/stanford'
ucla_1_test_dir = './data/test/ucla_1/'
ucla_2_test_dir = './data/test/ucla_2/'
maxmun_test_dir = './data/test/maxmun/'
caltech_test_dir = './data/test/caltech/'
sbl_test_dir = './data/test/sbl/'

for c in [pitt_dir,olin_dir,ohsu_dir,sdsu_dir,trinity_dir,um_1_dir,um_2_dir,
          usm_dir,yale_dir,cmu_dir,leuven_1_dir,leuven_2_dir,kki_dir,nyu_dir,
          stanford_dir,ucla_1_dir,ucla_2_dir,maxmun_dir,caltech_dir,sbl_dir,
          pitt_test_dir,olin_test_dir,ohsu_test_dir,sdsu_test_dir,
          trinity_test_dir,um_1_test_dir,um_2_test_dir,usm_test_dir,
          yale_test_dir,cmu_test_dir,leuven_1_test_dir,leuven_2_test_dir,
          kki_test_dir,nyu_test_dir,stanford_test_dir,ucla_1_test_dir,
          ucla_2_test_dir,maxmun_test_dir,caltech_test_dir, sbl_test_dir]:
    if not os.path.exists(c):
        os.mkdir(c)

train_files = glob(os.path.join(train_dir,"*.nii.gz"))    
for f in train_files:  
    if "Pitt" in f:
        shutil.move(f, pitt_dir)       
    if "Olin" in f: 
        shutil.move(f, olin_dir)            
    if "OHSU" in f: 
        shutil.move(f, ohsu_dir)
    if "SDSU" in f: 
        shutil.move(f, sdsu_dir)
    if "Trinity" in f: 
        shutil.move(f, trinity_dir)
    if "UM_1" in f: 
        shutil.move(f, um_1_dir)
    if "UM_2" in f: 
        shutil.move(f, um_2_dir)    
    if "USM" in f: 
        shutil.move(f, usm_dir)
    if "Yale" in f: 
        shutil.move(f, yale_dir)
    if "CMU" in f: 
        shutil.move(f, cmu_dir)        
    if "Leuven_1" in f: 
        shutil.move(f, leuven_1_dir)
    if "Leuven_2" in f: 
        shutil.move(f, leuven_2_dir)
    if "KKI" in f: 
        shutil.move(f, kki_dir)
    if "NYU" in f: 
        shutil.move(f, nyu_dir)
    if "Stanford" in f: 
        shutil.move(f, stanford_dir) 
    if "UCLA_1" in f: 
        shutil.move(f, ucla_1_dir)
    if "UCLA_2" in f: 
        shutil.move(f, ucla_2_dir)
    if "MaxMun" in f:
        shutil.move(f, maxmun_dir)        
    if "Caltech" in f: 
        shutil.move(f, caltech_dir)
    if "SBL" in f: 
        shutil.move(f, sbl_dir)

test_files = glob(os.path.join(test_dir,"*.nii.gz"))    
for f in test_files:  
    if "Pitt" in f:
        shutil.move(f, pitt_test_dir)       
    if "Olin" in f: 
        shutil.move(f, olin_test_dir)            
    if "OHSU" in f: 
        shutil.move(f, ohsu_test_dir)
    if "SDSU" in f: 
        shutil.move(f, sdsu_test_dir)
    if "Trinity" in f: 
        shutil.move(f, trinity_test_dir)
    if "UM_1" in f: 
        shutil.move(f, um_1_test_dir)
    if "UM_2" in f: 
        shutil.move(f, um_2_test_dir)    
    if "USM" in f: 
        shutil.move(f, usm_test_dir)
    if "Yale" in f: 
        shutil.move(f, yale_test_dir)
    if "CMU" in f: 
        shutil.move(f, cmu_test_dir)        
    if "Leuven_1" in f: 
        shutil.move(f, leuven_1_test_dir)
    if "Leuven_2" in f: 
        shutil.move(f, leuven_2_test_dir)
    if "KKI" in f: 
        shutil.move(f, kki_test_dir)
    if "NYU" in f: 
        shutil.move(f, nyu_test_dir)
    if "Stanford" in f: 
        shutil.move(f, stanford_test_dir) 
    if "UCLA_1" in f: 
        shutil.move(f, ucla_1_test_dir)
    if "UCLA_2" in f: 
        shutil.move(f, ucla_2_test_dir)
    if "MaxMun" in f:
        shutil.move(f, maxmun_test_dir)        
    if "Caltech" in f: 
        shutil.move(f, caltech_test_dir)
    if "SBL" in f: 
        shutil.move(f, sbl_test_dir)

#define common
masker = NiftiMapsMasker(maps_img=atlas_filename, standardize=True,
                         memory='nilearn_cache', verbose=5)
correlation_measure = ConnectivityMeasure(kind='correlation')

#generate graphs and save as numpy files for use in dataloader
for s in [pitt_dir,olin_dir,ohsu_dir,sdsu_dir,trinity_dir,um_1_dir,um_2_dir,
          usm_dir,yale_dir,cmu_dir,leuven_1_dir,leuven_2_dir,kki_dir,nyu_dir,
          stanford_dir,ucla_1_dir,ucla_2_dir,maxmun_dir,caltech_dir,sbl_dir,
          pitt_test_dir,olin_test_dir,ohsu_test_dir,sdsu_test_dir,
          trinity_test_dir,um_1_test_dir,um_2_test_dir,usm_test_dir,
          yale_test_dir,cmu_test_dir,leuven_1_test_dir,leuven_2_test_dir,
          kki_test_dir,nyu_test_dir,stanford_test_dir,ucla_1_test_dir,
          ucla_2_test_dir,maxmun_test_dir,caltech_test_dir, sbl_test_dir]:
    func_files = glob(os.path.join(s,"*_func_preproc.nii.gz"))    
    for idx in tqdm(range(len(func_files))):
        func_data = func_files[idx]
        sub_name = re.findall(r'_005\d+',func_data)[0]
        
        #extract time series
        time_series = masker.fit_transform(func_data, confounds=None)
        print('Time series in in the shape {0}'.format(time_series.shape))
        
        #create correlation matrices and view shape
        correlation_matrix = correlation_measure.fit_transform([time_series])
        print('Correlations are in an array of shape {0}'.format(correlation_matrix.shape))
        print(correlation_matrix)

        #save correlation matrix as numpy file
        corr_save = os.path.join(s, f'{sub_name}_correlations')
        np.save(corr_save, correlation_matrix, allow_pickle=True, fix_imports=True)
        
    #remove original 4D files; this step is optional
    #for f in func_files:      
    #    os.remove(f)
