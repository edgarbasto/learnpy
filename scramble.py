import os
import random

def scramble_files():
    #get file names
    file_list = os.listdir(r"/Users/edgar.basto/Documents/ISTEC Aulas/DDM-AED/scripts-aulas/learnpy/learnpy/prank")
    print(file_list)
    saved_path = os.getcwd()
    print("current path" +saved_path)
    os.chdir(r"/Users/edgar.basto/Documents/ISTEC Aulas/DDM-AED/scripts-aulas/learnpy/learnpy/prank")

    #scramble
    for file_name in file_list:
        print("Old Name - "+file_name)
        indexSplit = random.randrange(len(file_name))
        oldFileName = file_name.strip('.jpg')
        newFileName = str(random.randint(0,999999)) + oldFileName[:indexSplit] + str(random.randint(0,999999)) + oldFileName[indexSplit:] + str('.jpg')
        print("New Name - "+ newFileName)
        if file_name != '__MACOSX':
            os.rename(file_name, newFileName)
    os.chdir(saved_path)
    
scramble_files()
