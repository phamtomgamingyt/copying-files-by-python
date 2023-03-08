import os
import shutil
os.getcwd()
os.mkdir("files")
#splitingthe text
path = "C:/Users/harsh/Dropbox/PC/Desktop/lewis hamilton.txt"
root,extension = os.path.splitext(path)
print("The root element are" , root)
print("The extension is" , extension)
#os.listdir(path)
#making a copy of file /images
source = "C:/Users/harsh/Dropbox/PC/Desktop/lewis hamilton.txt"
destination = "C:/Users/harsh/Dropbox/PC/Desktop/copy-lewis hamilton.txt"
dest = shutil.copy(source,destination)
print("after copying the file")