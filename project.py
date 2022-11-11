import time
import os
import shutil

fromdir = "/Users/nehasharma/Downloads/testt"
todir = "/Users/nehasharma/Downloads/neha"
listOfFiles= os.listdir(fromdir)

for fileName in listOfFiles:
    name, extension = os.path.splitext(fileName)
    if extension == "":
        continue
    if extension in ['.txt','.pdf','.doc',]:
        path_1=fromdir+'/'+fileName
        path_2=todir+'/'+"documentFiles"
        path_3=todir+'/'+"documentFiles"+'/'+fileName
            
            
        if os.path.exists(path_2):
                print("directory exists")
                print("moving"+fileName+"...")
                shutil.move(path_1,path_3)
                time.sleep(1)
        else:
                print("making directory")
                os.makedirs(path_2)
                print("moving"+fileName+"...")
                shutil.move(path_1,path_3)
                time.sleep(1)

        



