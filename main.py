import os
import sys
import skimage

if __name__ == '__main__':

    #Check the args
    print("here are the passed arguments:")
    print(sys.argv)

    #Check the dependency requirements
    try:
        image = skimage.data.coins()
    except:
        print("dependencies specified in requirements.txt not installed")

    #Check the pretrain environment
    exists = os.path.exists("pretrain/pretrain.txt") and os.path.isfile("pretrain/pretrain.txt")

    if(exists):
        print("pretrain file imported sucessfully")
    else:
        print("error importing the pretrain file, it was not found.")