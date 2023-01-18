# A new file????? Yay!!!!!!!!!!
import random, os, shutil, glob, pathlib, inspect

# this function retreives varnames because W1THRD is lazy
def getName(var):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    return [var_name for var_name, var_val in callers_local_vars if var_val is var]

# This function filters the images by file type
def fileFilter(files: list, ext: str, dir: str) -> list:
    temp = []
    for item in files:
        if(item.endswith(ext)):
            temp.append("./default/textures/"+ dir + item)
    return(temp)

# This function replaces the ./default/ prefix of a filepath with ./Pack/assets/minecraft/
def dirSwap(dirs: list, swapmode: int) -> list:
    temp = []
    for item in dirs:
        temp.append("./Pack/assets/minecraft/"+"/".join(item.split("/")[2:15]))
    return(temp)

# This function indexes a list of Minecraft's textures, by type
# Currently, it only indexes: block, effect, item, map, mob_effect, particle, colormap, painting
def getImagesList() -> list:
    print("Finding images...")
    block = fileFilter(os.listdir("./default/textures/block/"), ".png", "block/")
    effect = fileFilter(os.listdir("./default/textures/effect/"), ".png", "effect/")
    item = fileFilter(os.listdir("./default/textures/item/"), ".png", "item/")
    mAp = fileFilter(os.listdir("./default/textures/map/"), ".png", "map/")
    particle = fileFilter(os.listdir("./default/textures/particle/"), ".png", "particle/")
    mob_effect = fileFilter(os.listdir("./default/textures/mob_effect/"), ".png", "mob_effect/")
    cm = fileFilter(os.listdir("./default/textures/colormap/"), ".png", "colormap/")
    pt = fileFilter(os.listdir("./default/textures/painting/"), ".png", "painting/")
    misc = fileFilter(os.listdir("./default/textures/misc/"), ".png", "misc/")
    env = fileFilter(os.listdir("./default/textures/environment/"), ".png", "environment/")
    return(block + effect + item + mAp + mob_effect + particle + cm + pt + misc + env)

# This function indexes a list of Minecraft's textures, to be randomized in a seperate group
def getILSep() -> list:
    print("Finding extra images...")
    entity = dirWalk("entity/") + dirWalk("models/armor/")
    gui = dirWalk("./default/textures/gui/")
    #Font randomization removed because it makes text mostly unreadable
    #fonts = fileFilter(os.listdir("./default/textures/font/"), ".png", "font/")
    fonts = []
    return([gui, fonts, entity])

# This function gets all of Minecraft's entity textures
def dirWalk(dir: str) -> list:
    temp = []
    for root, dirs, files in os.walk("./default/textures/" + dir):
        for file in files:
            if file.endswith(".png"):
                 temp.append(os.path.join(root, file).replace("\\", "/"))
    return(temp)

def shuffleFiles(files: list, swapmode: int):
    newLoc = ""
    temp = ""
    ori = files
    sh = dirSwap(files, swapmode)
    random.shuffle(sh)
    for i in range(len(ori)):
        shutil.copy(ori[i], sh[i])
    

# This function gets a list of all images to shuffle, shuffles it, and then renames all the files
def shuffleImages():
    print("Shuffling images...")
    ori = getImagesList()
    sh = dirSwap(getImagesList(), 0)
    random.shuffle(sh)
    
    for i in range(len(ori)):
        shutil.copy(ori[i], sh[i])

    print("Shuffling even more stuff...")
    ILSep = getILSep()
    for i in range(2):
        shuffleFiles(ILSep[i], 0)
        shuffleFiles(ILSep[2], 1)
        


