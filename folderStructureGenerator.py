import os

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
        

def generateBasicStructure():
    createFolder('./generated_files/')
    createFolder('./generated_files/www/')
    createFolder('./generated_files/database/')
    createFolder('./generated_files/www/css/')

def generateDynamicStructure(data):
    for i in data:
        createFolder('./generated_files/www/'+i)
