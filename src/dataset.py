

class ImageDataset:
    def __init__(self, root):
        self.root = root
        #get image paths
        #get paths to text file

    def __len__(self):
        #return # of images in object
        pass

    def __getitem__(self, idx):
        #read image path
        #read text file for bbox


        #return {image: tensor, bbox: box dimensions}
            #how does this work with variable # of objects in iamge?
        pass


#helper functions