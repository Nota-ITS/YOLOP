import os
import random
from pathlib import Path
from shutil import copyfile

# get root dir
root = 'C:\\Users\\NOTA\\Downloads'

# targets
imgs = '\\bdd100k_images_100k\\bdd100k\\images\\images'
det = '\\det_annotations\\data2\\zwt\\bdd\\bdd100k\\labels\\100k'
da = '\\da_seg_annotations\\bdd_seg_gt'
ll = '\\ll_seg_annotations\\bdd_lane_gt'

# train, val set numbers
TRAIN = 1400
VAL = 200

# random pick imgs from train set
train_list = random.sample(os.listdir(root+imgs+'\\train'), TRAIN)
val_list = random.sample(os.listdir(root+imgs+'\\val'),k=VAL)

# make dir
Path("/export/images/train").mkdir(parents=True, exist_ok=True)
Path("/export/images/val").mkdir(parents=True, exist_ok=True)

Path("/export/det_annotations/train").mkdir(parents=True, exist_ok=True)
Path("/export/det_annotations/val").mkdir(parents=True, exist_ok=True)

Path("/export/da_seg_annotations/train").mkdir(parents=True, exist_ok=True)
Path("/export/da_seg_annotations/val").mkdir(parents=True, exist_ok=True)

Path("/export/ll_seg_annotations/train").mkdir(parents=True, exist_ok=True)
Path("/export/ll_seg_annotations/val").mkdir(parents=True, exist_ok=True)

# copy target to destination dir
for a in train_list:
    copyfile(root+imgs+'\\train\\'+ a , f'/export/images/train/{a}')
    b = a.split('.')[0] + '.png'
    copyfile(root+da+'\\train\\'+ b , f'/export/da_seg_annotations/train/{b}')
    copyfile(root+ll+'\\train\\'+ b , f'/export/ll_seg_annotations/train/{b}')

    c = a.split('.')[0] + '.json'
    copyfile(root+det+'\\train\\'+ c , f'/export/det_annotations/train/{c}')

for a in val_list:
    copyfile(root+imgs+'\\val\\'+ a , f'/export/images/val/{a}')
    b = a.split('.')[0] + '.png'
    copyfile(root+da+'\\val\\'+ b , f'/export/da_seg_annotations/val/{b}')
    copyfile(root+ll+'\\val\\'+ b , f'/export/ll_seg_annotations/val/{b}')

    c = a.split('.')[0] + '.json'
    copyfile(root+det+'\\val\\'+ c , f'/export/det_annotations/val/{c}')