import os
from os.path import isfile, join
import re

import torchvision

class ImageDataset:
    def __init__(self, root, transforms = None):
        self.root = root
        self.images = get_paths(root + "images/")
        
        self.bboxes = get_paths(root + "labels/")
        self.transforms = transforms

    def __len__(self):
        #return # of images in object
        return len(self.images)

    def __getitem__(self, idx):
        image = torchvision.io.read_image(self.images[idx], mode = torchvision.io.ImageReadMode.RGB)
        #read image path
        bbox = []
        with open(self.bboxes[idx]) as file:
            for line in file:
                bbox.append(line)
        bbox = [s.strip('\n') for s in bbox]

        sample = {}
        sample['id'] = re.sub(r'(^0+)|(.txt)', "", self.bboxes[idx])
        sample['image'] = image
        sample['bboxes'] = bbox
        return sample

#helper functions
def get_paths(directory): 
    paths = [(directory + f) for f in os.listdir(directory) if isfile(join(directory, f))]
    return sorted(paths)


