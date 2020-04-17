# organize dataset into a useful structure
from os import makedirs
from os import listdir
from shutil import copyfile
from random import seed
from random import random
# create directories
dataset_home = 'dataset/'
subdirs = ['train/', 'test/']
for subdir in subdirs:
    # create label subdirectories
    labeldirs = ['Drowsiness/', 'Heartattack/' ,'No_Gesture' ,'Plam_Gesture', 'Victory_Gesture']
    for labldir in labeldirs:
        newdir = dataset_home + subdir + labldir
        makedirs(newdir, exist_ok=True)
# seed random number generator
seed(1)
# define ratio of pictures to use for validation
val_ratio = 0.25
# copy training dataset images into subdirectories
src_directory = 'trainingset/'
for file in listdir(src_directory):
    src = src_directory + '/' + file
    dst_dir = 'train/'
    if random() < val_ratio:
        dst_dir = 'test/'
    if file.startswith('Drowsiness'):
        dst = dataset_home + dst_dir + 'Drowsiness/'  + file
        copyfile(src, dst)
    elif file.startswith('Heartattack'):
        dst = dataset_home + dst_dir + 'Heartattack/'  + file
        copyfile(src, dst)
    elif file.startswith('No_Gesture'):
        dst = dataset_home + dst_dir + 'No_Gesture/'  + file
        copyfile(src, dst)
    elif file.startswith('Plam_Gesture'):
        dst = dataset_home + dst_dir + 'Plam_Gesture/'  + file
        copyfile(src, dst)
    elif file.startswith('Victory_Gesture'):
        dst = dataset_home + dst_dir + 'Victory_Gesture/'  + file
        copyfile(src, dst)