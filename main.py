import os

#Color variations
dir_list = ['17640755',
           '17593555',
           '16869934',
           '15737113',
           '16928431',
           '16867075',
           '15737114',
           '16414990',
           '15679788',
           '18689746',
           '17640770',
           '16445773',
           '17404501']

#Folder path (use double slash \\ between folders)
parent_dir = f"F:\\PC\\Work\\Job alphaar.io\\3D Artist\\Autry Medalist\\Variations"

def AddAdditionalDir(path):
    try:
        os.makedirs(os.path.join(path, "Left"), exist_ok=True)
        os.makedirs(os.path.join(path, "Right"), exist_ok=True)
    except OSError as error2:
        print('We have an issue')

def AddInnerDir(path, dir):
    try:
        os.makedirs(path, exist_ok=True) #If exist_ok=False gonna return ERROR, then folder already exist
        os.makedirs(os.path.join(path, "Texture"), exist_ok=True)
        AddAdditionalDir(os.path.join(path, "Texture"))
        os.makedirs(os.path.join(path, dir), exist_ok=True)
        AddAdditionalDir(os.path.join(path, dir))
    except OSError as error:
        print('We have an issue')

for dir in dir_list:
    path = os.path.join(parent_dir, dir)
    AddInnerDir(path,dir)