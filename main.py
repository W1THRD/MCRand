import json, random
from collections import OrderedDict 
  
with open('input.json') as infile:
    data = json.load(infile)  

keys = list(data.keys())
random.shuffle(keys)
newData = dict(zip(keys, data.values()))

json_object = json.dumps(newData, indent=4)
with open("./Pack/assets/minecraft/lang/en_us.json", "w") as outfile:
    outfile.write(json_object)

print("Done!")
input("Press Enter to quit")
