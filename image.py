#!/usr/bin/python
import os, sys, numpy
from PIL import Image

def getBinaryData(filename):
    
    os.chdir('/home/ubuntu/Code/learn')
    binaryValues=[]
    files=open(filename, 'r')
    data=files.read(65536)
    for character in data:
        result=ord(character)
        binaryValues.append(result)   
    return binaryValues
 
def creatGreyScaleImageSpecific(dataSet, outputfilename, width=0):
    image=Image.new('L', (256, 256))
    image.putdata(dataSet)  
    imagename=outputfilename+".png"
    os.chdir("/home/ubuntu/Code/image/")
    image.save(imagename)
    print(imagename+" Greyscle image created")

if __name__=="__main__":
  file_dir=r"/home/ubuntu/Code/learn"
  files=os.listdir(file_dir) #save filename_list
  for i in files[:10]:
    base_name=os.path.splitext(i)[0]
    outputfilename=os.path.join("/home/ubuntu/Code/image",base_name)
    binaryData=getBinaryData(i)
    creatGreyScaleImageSpecific(binaryData, outputfilename)
    


  



