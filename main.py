import pypokedex
from mojang import MojangAPI
true = MojangAPI.get_uuid("") #put your mc username
if true:
    print("false")
else:
    print("true")
var = 0o01 #no running literals lol so you have to do this goofy mess
lol = 1000
for i in range(lol):
    p = pypokedex.get(dex=var)
    p-name = p.name
    true = MojangAPI.get_uuid(p-name)
    if not true:
        print(p-name)
    
        
    var = var + 1
