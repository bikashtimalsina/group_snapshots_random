import os
import shutil
import glob
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from pathlib import Path
folders=glob.glob("./configuration/[0-9]*")
shuffled_folders=shuffle(folders)
snapshots_9=train_test_split(shuffled_folders, test_size=0.045)
snapshots_19=train_test_split(shuffled_folders,test_size=0.1)
snapshots_28=train_test_split(shuffled_folders,test_size=0.145)
snapshots_38=train_test_split(shuffled_folders,test_size=0.2)
snaplist=[snapshots_9,snapshots_19,snapshots_28,snapshots_38]
snapfolder=['snap9','snap19','snap28','snap38']
shufflefolder="./shufflesnapshots"
path=Path(shufflefolder)
if path.is_file():
    shutil.rmtree(shufflefolder)
if not path.is_file():
    os.mkdir(shufflefolder)
    snapeach=[shufflefolder+'/'+snapf for snapf in snapfolder]
    for i in range(len(snapeach)):
        os.mkdir(snapeach[i])
        for j in range(len(snaplist[i][1])):
            #shutil.copytree(snaplist[i][1][j],snapeach[i]+"/")
            os.system("cp -rf {} {}".format(snaplist[i][1][j],snapeach[i]))
