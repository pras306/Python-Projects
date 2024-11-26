import os, shutil

path = r"C:/Users/pras3/source/Workspace/data-analyst-projects/Python-Projects/automate-file-sorter/Files/"

file_names = os.listdir(path)
print(file_names)

for file in file_names:
    file_extension = os.path.splitext(file)[1][1:].upper()
    print(file_extension)

    try:
        if os.path.exists(path + file_extension + "Files"):
            shutil.move(path + file, path + file_extension + "Files/" + file)
            pass

        if not os.path.exists(path + file_extension + "Files"):
            os.makedirs(path + file_extension + "Files")
            shutil.move(path + file, path + file_extension + "Files/" + file)
            pass
        pass
    except:
        print('There are files in this path that were not moved.')
        pass

    pass
