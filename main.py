import pypokedex
from mojang import MojangAPI
true = MojangAPI.get_uuid("jokkwggwgwg")
if true:
    print("faslt")
else:
    print("true")
var = 0o01 #no running literals lol so you have to do this goofy mess
lol = 1000
for i in range(lol):
    p = pypokedex.get(dex=var)
    sussy = p.name
    true = MojangAPI.get_uuid(sussy)
    if not true:
        print(sussy)
    
        
    var = var + 1
