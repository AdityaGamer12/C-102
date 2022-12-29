import os
import shutil

#source ="copy"
#dstn ="paste"

from_dir = "C:/Users/Aditya/Downloads"
to_dir = "paste"

list_of_files = os.listdir(from_dir)

print(list_of_files)

for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)

    if extension =='':
       continue
    if extension in ['.gif','.png','.jpg','jpeg','.jfif']:

        path1 = from_dir + '/' + file_name

        path2= to_dir + '/' + "Image_Files"

        path3= to_dir + '/' + "Image_Files" + '/' + file_name


        if os.path.exists(path2):
            print("Moving" + file_name + ".....")


            shutil.move(path1,path3)

        else:
            os.makedirs(path2)
            print("Moving" + file_name + ".....")
            shutil.move(path1,path3)