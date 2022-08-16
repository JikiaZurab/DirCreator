import os

#List of folders that's gonna be created 
dir_list = ['14697228',
           '14697155',
           '17258333']

#Folder path (use double slash \\ between folders)
parent_dir = f"F:\\PC\\Work\\Job alphaar.io\\3D Artist\\Burberry logo-print Vintage"
parent_dir = os.path.join(parent_dir,"Variation")
os.makedirs(parent_dir, exist_ok=True)

def AddAdditionalDir(path):
    try:
        os.makedirs(os.path.join(path, "Left"), exist_ok=True)
        os.makedirs(os.path.join(path, "Right"), exist_ok=True)
    except OSError as error2:
        print('We have an issue with inner directory')

def AddInnerDir(path, dir):
    try:
        os.makedirs(path, exist_ok=True) #If exist_ok=False gonna return ERROR, then folder already exist
        os.makedirs(os.path.join(path, "Texture"), exist_ok=True)
        AddAdditionalDir(os.path.join(path, "Texture"))
        os.makedirs(os.path.join(path, dir), exist_ok=True)
        AddAdditionalDir(os.path.join(path, dir))
    except OSError as error:
        print('We have an issue with main directories')

for dir in dir_list:
    path = os.path.join(parent_dir, dir)
    AddInnerDir(path,dir)