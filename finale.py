"""
FINALE HACK@2021
AUTORE: Raffaele Ruggeri
data 16/12/2021
"""
class ogg: 
    def __init__(self,ID=None,time_prod=None,time_trasp=None,dip=None): 
        self.ID = ID
        self.time_prod = time_prod
        self.time_trasp = time_trasp
        self.dip = dip
    def __str__(self):
        return  f'({self.ID},{self.time_prod},{self.time_trasp},{self.dip})'
class final_ogg(ogg): 
    def __init__(self,ID=None,time_prod=None,time_trasp=None,dip=None,time_limit= None,value= None): 
        ogg.__init__(self,ID,time_prod,time_trasp,dip)
        self.time_limit = time_limit 
        self.value = value
    def __str__(self):
        return f'({self.ID},{self.time_prod},{self.time_trasp},{self.dip},{self.time_limit},{self.value})'
def getter():
    dic_ogg =  {}
    dic_final_ogg = {}
    ls = [riga.split(" ") for riga in open("input", "r").read().split("\n")[:-1]]
    n_ogg, ogg_fin, chains = list(map(int,ls[0]))
    for riga in sorted(ls[1:], key = lambda x : -len(x)):
        if len(riga) > 3:
            dic_ogg.setdefault(riga[0], ogg(riga[0],int(riga[1]),int(riga[2]),[]))
            for i in range(1, int(riga[3])+1):
                dic_ogg[riga[0]].dip.append(riga[3+i])
        else:
            old = dic_ogg[riga[0]]
            dic_final_ogg.setdefault(riga[0], final_ogg(old.ID, old.time_prod, old.time_trasp, old.dip, int(riga[1]), int(riga[2])))
            del dic_ogg[riga[0]]
    return chains, dic_ogg, dic_final_ogg

def rec(ls_obj, chains, where, catena, file):
    for obj in ls_obj:
        catena[where] += 1
        if obj.dip != []: rec(obj.dip, chains, where,catena,file)
        where = 0
        file.write(f'{obj.ID} {chains-1-where}\n')
     
def fun():
    f = open("out.txt", "w+")
    f.write("")
    f.close()
    file = open("out.txt", "a")
    chains, dic_ogg, dic_final_ogg = getter()
    catena = [0]*chains
    dic_final_ogg = dict(sorted(dic_final_ogg.items(), key = lambda x : (len(x[1].dip),x[1].time_prod, x[1].time_trasp, x[1].value, x[1].time_limit)))
    for key, OBJ in dic_ogg.items():
        for i in range(len(OBJ.dip)):
            dic_ogg[key].dip[i] = dic_ogg[dic_ogg[key].dip[i]] 
    for key, OBJ in dic_final_ogg.items():
        for i in range(len(OBJ.dip)):
            dic_final_ogg[key].dip[i] = dic_ogg[dic_final_ogg[key].dip[i]]
    for key, OBJ in dic_final_ogg.items():
        where = catena.index(min(catena))
        catena[where] += 1
        rec(OBJ.dip, chains, where,catena, file)
        file.write(f'{OBJ.ID} {chains-1-where}\n')
    print(catena)
    
fun()

















