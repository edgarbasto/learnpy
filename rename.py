import os

def rename_files():
    #get file names
    file_list = os.listdir(r"C:\Users\edgar\Documents\Git\learnpython\prank")
    print(file_list)
    saved_path = os.getcwd()
    print("current path" +saved_path)
    os.chdir(r"C:\Users\edgar\Documents\Git\learnpython\prank")

    #rename
    for file_name in file_list:
        print("Old Name - "+file_name)
        print("Old Name - "+file_name.strip('0123456789'))
        os.rename(file_name, file_name.strip('0123456789'))
    os.chdir(saved_path)

rename_files()
