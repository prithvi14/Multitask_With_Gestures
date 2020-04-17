AZSA# organize dataset into a useful structure
from os import makedirs
from os import listdir
from shutil import copyfile
# create directories
dataset_home = 'finalizedataset/'
# create label subdirectories
labeldirs = ['Drowsiness/', 'Heartattack/']
for labldir in labeldirs:
	newdir = dataset_home + labldir
	makedirs(newdir, exist_ok=True)
# copy training dataset images into subdirectories
src_directory = 'trainingset/'
for file in listdir(src_directory):
	src = src_directory + '/' + file
	if file.startswith('Drowsiness'):
		dst = dataset_home + 'Drowsiness/'  + file
		copyfile(src, dst)
	elif file.startswith('Heartattack'):
		dst = dataset_home + 'Heartattack/'  + file
		copyfile(src, dst)