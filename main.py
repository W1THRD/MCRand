# Here is my overly-messy code...
import json, random, textures
from collections import OrderedDict 

# Small Text Randomizer
print("Processing small texts...")
with open('./default/lang/en_us.json') as infile:
    data = json.load(infile)  

keys = list(data.keys())
random.shuffle(keys)
newData = dict(zip(keys, data.values()))

json_object = json.dumps(newData, indent=4)
with open("./Pack/assets/minecraft/lang/en_us.json", "w", encoding="utf8") as outfile:
    outfile.write(json_object)
# Long text randomizer
print("Processing large texts...")
end = [] # 151 lines (end poem)
with open("./default/texts/end.txt", encoding="utf8") as file: 
    for line in file:
        end.append(line.rstrip())
splashes = [] # 440 lines (splash text)
with open("./default/texts/splashes.txt", encoding="utf8") as file: 
    for line in file:
        splashes.append(line.rstrip())
postc = [] # 6 lines (text at the end of the credits)
with open("./default/texts/postcredits.txt", encoding="utf8") as file: 
    for line in file:
        postc.append(line.rstrip())
full = end + splashes + postc # 597 lines
random.shuffle(full)
# splitting long texts/clearing files/saving them
end = full[0:151]
splashes = full[152:592]
postc = full[593:599] # something broke, but oh well

with open("./Pack/assets/minecraft/texts/end.txt",'r+', encoding="utf8") as file:
    file.truncate(0)
with open('./Pack/assets/minecraft/texts/end.txt', 'w', encoding="utf8") as f:
    for line in end:
        f.write(f"{line}\n")

with open("./Pack/assets/minecraft/texts/splashes.txt",'r+', encoding="utf8") as file:
    file.truncate(0)
with open('./Pack/assets/minecraft/texts/splashes.txt', 'w', encoding="utf8") as f:
    for line in splashes:
        f.write(f"{line}\n")

with open("./Pack/assets/minecraft/texts/postcredits.txt",'r+', encoding="utf8") as file:
    file.truncate(0)
with open('./Pack/assets/minecraft/texts/postcredits.txt', 'w', encoding="utf8") as f:
    for line in postc:
        f.write(f"{line}\n")
# Randomizing images
textures.shuffleImages()


print("Done!")
input("Press Enter to quit")
