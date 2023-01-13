# A new file????? Yay!!!!!!!!!!
import random, os, shutil

# This function filters the images by file type
def fileFilter(files: list, ext: str, dir: str) -> list:
    temp = []
    for item in files:
        if(item.endswith(ext)):
            temp.append("./default/textures/"+ dir + item)
    return(temp)

# This function replaces the ./default/ prefix of a filepath with ./Pack/assets/minecraft/
def dirSwap(dirs: list) -> list:
    temp = []
    for item in dirs:
        temp.append("./Pack/assets/minecraft/"+"/".join(item.split("/")[2:5]))
    return(temp)

# This function indexes a list of Minecraft's textures, by type
# Currently, it only indexes: block, effect, item, map, mob_effect, particle
def getImagesList() -> list:
    print("Finding images...")
    block = fileFilter(os.listdir("./default/textures/block/"), ".png", "block/")
    effect = fileFilter(os.listdir("./default/textures/effect/"), ".png", "effect/")
    item = fileFilter(os.listdir("./default/textures/item/"), ".png", "item/")
    mAp = fileFilter(os.listdir("./default/textures/map/"), ".png", "map/")
    mob_effect = fileFilter(os.listdir("./default/textures/mob_effect/"), ".png", "mob_effect/")
    particle = fileFilter(os.listdir("./default/textures/particle/"), ".png", "particle/")
    return(block + effect + item + mAp + mob_effect + particle)

# This function gets a list of all images to shuffle, shuffles it, and then renames all the files
def shuffleImages():
    print("Shuffling images...")
    ori = getImagesList()
    sh = dirSwap(getImagesList())
    random.shuffle(sh)
    
    for i in range(len(ori)):
        #print(ori[i] + " -> " + sh[i])
        shutil.copy(ori[i], sh[i])
        


