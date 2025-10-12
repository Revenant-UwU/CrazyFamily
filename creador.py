import random
from typing import TypedDict, List
import numpy as np
from enum import Enum
class oficios(Enum):
    Void = 0
    Patriarca= 1
    Matriarca= 2
    Cazador= 3
    Buzcador_a= 4
    Estudiante= 5
class Personalidad(TypedDict):
    Principal: List[any]
    Secundaria: List[any]
def normalizador_dic(dic):
    # Convertir a arrays ordenados
    x = np.array(sorted(dic.keys()))
    y = np.array([dic[k] for k in sorted(dic.keys())])
    # Interpolamos de 0 a 100
    x_new = np.arange(0, 101)  # de 0 a 100
    y_new = np.interp(x_new, x, y)
    # Resultado: diccionario uniforme
    result= {i: round(p, 2) for i, p in zip(x_new, y_new)}
    return result

perosnalidades_p =("Generous", "Brave", "Honest", "Greedy", "Cowardly", "Manipulative")
morlidad_v= {"Generous": 10, "Brave": 12, "Honest": 8, "Greedy":7, "Cowardly":5, "Manipulative":3,
             "Confident":4, "Shy": -5, "Repulsive": -9, "Charming":random.choice([0, 8, -11]), "Lustful":random.choice([11 ,-8,0, 8, -11]),
             "Inocent":random.choice([0,6, -5]), "Sadistic": -12, "Masochistic":-12, "Violent": -20, "Pacifist": 20,
             "Chad": random.choice([None, 12, 13]),"Twink":None,"Sex-deprived": random.randrange(-29,-7 ), "Pedofile": random.choice([random.randrange(10,25), random.randrange(-99, 0) ]),
             "Sex-apeal":random.choice([12, 13]), "Incel": -5, "Femcel": -3 , "Sweat home alabama": -20, "Zoofile": random.choice([random.randrange(10,25), random.randrange(-30, 10)]),
             "Futa": 0, "Healty": random.randrange(-2,3), "Sick": random.randrange(-3,3), "Albino": random.randrange(-9, 20), "Malformation": random.randint(-27, 20), 
             "Heavy-malformation": random.choice([10 ,8, 6, 4, 2, 0, -1, -15, -91]), "Hermafrodite": random.randrange(-19,8 ),  "Younght": 30, "Old": 0,
             "Infertil": 0, "Gay": random.randrange(-25, 25), "Fragile": random.randrange(-10,10),
             "Focused":10, "Unfocused":-2, "Disasiotive":-30, "Anger-Issues":-10, "Creative": random.choice([-10,20, 22]),
             "Depresive": random.randrange(-5, 5), "Masked": random.randrange(-30,0), "Depending": 1, 
             "Hero-complex": random.choice([-30,30]), "Edipo-complex": random.randrange(-30, 3)
             }
perosnalidades_s = {"Mental": ("Focused", "Unfocused", "Disasiotive", "Anger-Issues", "Creative", "Depresive", "Masked", "Depending", "Hero-complex", "Edipo-complex"), 
                    "Fisical": ("Healty", "Sick", "Albino", "Malformation", "Heavy-malformation", "Hermafrodite", "Younght", "Old", "Infertil", "Fragile"), 
                    "Sexual": ("Chad", "Twink", "Sex-deprived", "Pedofile", "Sex-apeal", "Incel", "Femcel", "Sweat home alabama", "Zoofile", "Futa", "Gay"),
                    "Talent": ("Confident", "Shy", "Repulsive" , "Charming" ,"Lustful","Inocent" , "Sadistic", "Masochistic", "Violent", "Pacifist")} #Charming used as fetile 
from adn_code import *
original_1 = {0:0, 4:1 , 9:5, 12:7, 14:13, 16:20, 18:22, 25:20, 30:18, 40:7, 50:5, 80:1, 300:1}
original_2={0:0, 9:1, 11:10, 20:25, 40:20, 50:10, 100:1, 300:1}
fertilidad_por_edad_f = normalizador_dic(original_1)
fertilidad_por_edad_m = normalizador_dic(original_2)
for i in range(101, 200):
    fertilidad_por_edad_f[i] = 20.0
    fertilidad_por_edad_m[i] = 20.0

NPC_vivos = [] #lista de objetos persona
NPC_muertos= []
NPC_infertil= []
Familias = [] #lista de objetos familia
Familias_nombres = []
Nombres_NPC = []
def random_name(length_n):
    letters= { "vocals": ['a','e','i', "o", "u"],
    "consonants": 
    ["b","c","d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]}
    name=[]
    s=0
    while len(name)<length_n:
        s+= 1
        if name == []:
            if random.random() == 1:
                name.append(random.choice(letters["vocals"]).upper())
            else:
                name.append(random.choice(letters["consonants"]).upper())
        if (name[-1].lower() in letters["vocals"] and random.random() == 1) or (name[-1].lower() in letters["consonants"]):
            new = random.choice(letters["vocals"])
            if len(name) > 2 and new == name[-1].lower:
                new = random.choice(letters["vocals"])
            name.append(new)
        elif name[-1].lower() in letters["vocals"]:
            name.append(random.choice(letters["consonants"]))
        if s//2 > length_n:
            raise TimeoutError(name)
    s=''
    return s.join(name)
class Persona:
    def __init__(self, nombre:str, Family, edad:int, genero:str, personalidad:Personalidad , oficio:oficios , madre, padre, moralidad = None):
        self.nombre = nombre
        self.nombre_familia = Family.nombre_familia
        self.familia:Familia = Family
        self.edad = int(edad)
        self.genero = genero
        if oficio == None:
            self.oficio:oficios = oficios.Void
        elif oficio in oficios.__members__:
            self.oficio:oficios = oficios[oficio]
        else:
            raise TypeError(f'Wrong office mf {self},{oficio}')
        self.madre:Persona = madre
        self.padre:Persona = padre
        self.adn: ADN= None
        self.social = {'Liked': [], 'Disliked': []}
        hambre = 50
        sed =50
        self.estomago = [hambre, sed]
        self.health_max = 100
        if personalidad != None:
            self.personalidad:Personalidad = personalidad #Primaria list, secundaria list too 
            if madre == None or padre == None:
                self.adn = ADN(personalidad["Principal"][0], personalidad["Principal"][1])
            else:
                self.adn = ADN(personalidad["Principal"][0], personalidad["Principal"][1], None, create_lore(madre.adn, padre.adn))
        else:
            if padre == None or madre == None:
                raise ValueError('Not enough data to creat a person: Missing personlaidad or fathers')
            self.adn = ADN(None, None, None, create_lore(madre.adn, padre.adn))
            deco = deconstusct(self.adn)
            self.personalidad = {"Principal": deco[0], "Secundaria": deco[1]}
        self.moralidad = moralidad
        if self.moralidad == None:
            self.moralidad= self.calculo_morlidad()
        for b in self.personalidad["Secundaria"]:
            if b == 'Healty' :
                self.health_max += 15
            if b == "Younght":
                self.health_max += 10
            if b == 'Sick':
                self.health_max -=10
            if b == 'Malformation':
                self.health_max -= 15
            if b == 'Heavy-malformation':
                self.health_max -=30
            if b == 'Old':
                self.health_max -=10
            if b == 'Fragile':
                self.health_max -=20
        self.healt = self.health_max
        NPC_vivos.append(self)
    def __str__(self):
        nombre = self.nombre + '. ' + self.nombre_familia
        if self.healt > 0:
            if self.oficio in [oficios.Patriarca, oficios.Matriarca]:
                nombre = '\033[32m' + nombre + '\033[0m' 
            elif self.oficio in [oficios.Cazador, oficios.Buzcador_a]:
                nombre = '\033[35m' + nombre + '\033[0m' 
        return f"{nombre}, {self.edad}, {self.genero}"
    def __repr__(self):
        if self.oficio in [oficios.Patriarca, oficios.Matriarca]:
            return f'\033[32m{self.nombre}. {self.nombre_familia}\033[0m'
        elif self.oficio in [oficios.Cazador, oficios.Buzcador_a]:
            return f'\033[35m{self.nombre}. {self.nombre_familia}\033[0m'
        return f"{self.nombre}. {self.nombre_familia[0]}"
    def muerte(self):
        hambre = self.estomago[0]
        sed = self.estomago[1]
        for i in [hambre, sed]:
            if i<10:
                if i <3:
                    self.healt -=10
                else:
                    self.healt -=random.choice(range(2,5))
        if self.healt <=0 :
            print('\n\033[31m', '*'*60)
            print(f' \t No puede ser \n \t \t {self}\033[31m MURIO ' )
            print('edad: ',self.edad, '\nestomago', self.estomago,'\nsalud', self.healt,'\nmax salud', self.health_max,'\npersonalidad', self.personalidad)
            print('\n', '*'*60, '\033[0m')
            NPC_vivos.remove(self)
            NPC_muertos.append(self)
            self.familia.remove(self)
            if self.oficio in [oficios.Matriarca, oficios.Patriarca]:
                self.familia.choice_new_lider(self)
        elif hambre > 0 and sed > 0:
            h:float = self.health_max * (0.02-(self.edad/1000))
            if self.healt + h > self.health_max:
                self.healt = self.health_max
            else:
                if self.healt >= self.health_max * 0.2:
                    self.healt += h
                else:
                    self.healt += self.healt
        for i in [0,1]: self.estomago[i] -= (random.randrange(5+(2*(self.edad//20)),15+(2*(self.edad//20))))
    def calculo_morlidad(self):
        m = 0
        p = []
        if self.personalidad != None:
            for i in self.personalidad:
                if self.personalidad[i] != None:
                    for b in self.personalidad[i]:
                        p.append(b)
                else:
                    p.append(None) 
            for peppepepepe in p:
                if peppepepepe != None:
                    if morlidad_v[peppepepepe] == None:
                        m += random.randrange(-100,100)
                    else:
                        m += morlidad_v[peppepepepe]
                else:
                    m += 0
        else:
            m = self.moralidad
        return m
class Animal:
    def __init__(self, nombre):
        self.nombre:str = nombre
        self.genes:str = None
        self.get_genes()
    def __str__(self):
        return f"{self.nombre}, an animal"
    def __repr__(self):
        return f"{self.nombre}: Animal"
    def get_genes(self):
        '''
        types: dog, cat, horse, dragon, pig
        '''
        n = self.nombre.lower()
        if 'dog' in n:
            genes = ADN('dog')
        elif "cat" in n:
            genes = ADN('cat')
        elif "horse" in n:
            genes = ADN('horse')
        elif 'dragon' in n:
            genes = ADN('dragon')
        elif 'pig' in n:
            genes = ADN('pig')
        else:
            raise NameError('the name given to the animal doesnt indicate the animal it is suposed to be', n)
        self.genes = genes
class Pareja(Persona):
    def __init__(self, persona:Persona, pareja = None):
        if not isinstance(persona, Persona) and not isinstance(persona, Animal):
            raise TypeError(f"{persona}, is not a subclass of Persona or Animal")
        super().__init__(persona.nombre, persona.familia, persona.edad, persona.genero, persona.personalidad, persona.oficio, persona.madre, persona.padre)
        self.pareja:Pareja = pareja
        #Ahora busca donde estan todos sus hijos para remplazar el padre/madre por ellos.

        for lista in NPC_muertos, NPC_vivos, NPC_infertil:
            i = 0
            if lista != []:
                for Npc in lista:
                    if not isinstance(Npc, Persona):
                        raise TypeError(f"{Npc}, {lista}")
                    if Npc.padre is not None:
                        if Npc.padre.nombre == self.nombre: 
                            Npc.padre = self
                    if Npc.madre is not None:    
                        if Npc.madre.nombre == self.nombre:
                            Npc.madre = self
                    if Npc.nombre == self.nombre:
                        npc_to_remplace = i
                    i += 1
                lista[npc_to_remplace] = self
    def __str__(self):
        return super().__str__() + " Pareja" + f" with {self.pareja[0]}"
    def __repr__(self):
        return super().__repr__() + f" with {self.pareja[0]}"
class Familia:
    def __init__(self, nombre_f = 'NUL'):
        '''Crea familia vacia'''
        self.nombre_familia:str = nombre_f
        self.personalidad:list = []
        self.funcionamiento:str = "" 
        self.miembros:list = []
        self.gene: ADN
    def constructor_familia(self):
        '''crea familia random'''
        self.personalidad = selector_p_prin()
        self.nombre_familia = random_name(random.randrange(4,10))
        self.nombre_familia = name_not_in_list(self.nombre_familia, Familias_nombres, 4, 10)
        nombre = name_not_in_list(random_name(random.randrange(5,8)), Nombres_NPC, 5, 8)
        nombrem = name_not_in_list(random_name(random.randrange(5,8)), Nombres_NPC, 5, 8)
        self.funcionamiento = random.choice(['P', 'M'])
        if self.funcionamiento == 'P':
            i = 0
            a = 1
        else:
            i = 1
            a = 0
        Patriarca = Persona(nombre, self, random.randint(45,80), 'M', {"Principal": [self.personalidad[i], self.personalidad[a]], "Secundaria": []}, "Patriarca", None, None)
        Matriarca = Persona(nombrem, self, random.randint(45,80), 'F', {"Principal": [self.personalidad[a], self.personalidad[i]], "Secundaria": []}, "Matriarca", None, None)
        self.miembros.append(Patriarca)
        self.miembros.append(Matriarca)
        Familias.append(self)
        while len(self.miembros) <= 8:
            born(SEXO(self.miembros))
            i: Persona
            for i in self.miembros:
                i.edad += 1
    def add(self, persona:Persona):
        if persona.familia != self:
            raise KeyError(f'{persona} has another family: {persona.familia}')
        if persona in self.miembros:
            raise ValueError(f'{persona} already in famiily')
        self.miembros.append(persona)
    def remove(self,persona:Persona):
        if persona not in self.miembros:
            raise ValueError(f'{persona} not in famiily')
        self.miembros.remove(persona)
    def choice_new_lider(self, persona:Persona):
        if persona.oficio in [oficios.Patriarca, oficios.Matriarca]:
            sortage = sorted(self.miembros, key=lambda p: p.edad, reverse=True)
            candidato = None
            i = 0
            try:
                if persona.oficio == oficios.Patriarca:
                    while candidato == None:
                        if sortage[i].genero != 'M':
                            i+=1
                        else:
                            candidato = sortage[i]
                        if i >= len(sortage):
                            raise IndexError
                else:
                    while candidato == None:
                        if sortage[i].genero != 'F':
                            i+=1
                        else:
                            candidato = sortage[i]
                        if i >= len(sortage):
                            raise IndexError
                candidato.oficio = persona.oficio
            except:
                print('No abilavble candidats after ', persona,' died ', persona.oficio.name, ' is empty now')
        else:
            raise TypeError
    def count_ofices(self,ofice):
        i: Persona
        b = 0
        for i in self.miembros:
            if i.oficio == ofice:
                b +=1
        return b
    def __repr__(self):
        return f'{self.nombre_familia}, {self.funcionamiento}, {len(self.miembros)}'
def selector_p_prin():
    p = []
    while len(p) < 2: 
        pe = random.choice(perosnalidades_p)
        if pe not in p: 
            p.append(pe) 
    return p
def name_not_in_list(name:str, list:list, rerrol1:int, rerrol2:int) -> str: 
    while name in list:
        name= random_name(random.randint(rerrol1, rerrol2))
    list.append(name)
    return name
def SEXO(integrantes):
    """
    Junta a todos los integrantes del sexo y los hace tener sexo con multiples resultados
    pre: persona, pareja, animal
    post: diccionario de todas las mujeres embarazadas y con quien, {mujer: pareja}/ {animal: pareja}
    """

    Intentos = {}
    def intento_exito(probabilidad: float) -> bool:
        """
        Devuelve True si se tiene éxito con la probabilidad dada (0 a 100).
        """
        ran = random.uniform(0, 100) 
        prob = 100 -  probabilidad
        return ran < prob
    def creampie(male, fertility):
        embarazo = False
        fertilidad_f = 100 - fertility
        if isinstance(male, Persona):
            if male.oficio != 'Patriarca':
                fertilidad_m = fertilidad_por_edad_m[int(male.edad)]
            else:
                fertilidad_m = 100
            while Intentos[male] > 0 and embarazo != True:
                chance = fertilidad_f * (fertilidad_m/100)
                chance2 = 100 - chance
                embarazo= intento_exito(chance2)
                Intentos[male] -= 1
                if embarazo:
                    
                    return embarazo
        else:
            while Intentos[male] > 0 and embarazo != True:
                chance = fertilidad_f * (random.randrange(5,15)/100)
                chance2 = 100 - chance 
                embarazo = intento_exito(chance2)
                Intentos[male] -= 1
                if embarazo:
                    return embarazo
    def calcular_intentos(male):
        if isinstance(male, Persona):
            if int(male.edad) >11 and int(male.edad) <25:
                    intentos = random.choice([1,1,2,2,3])
            else: 
                intentos = 1
        else:
             intentos = random.choice([1,2])
        return intentos
    mujeres=0
    Mu = []
    Hom= []
    animales=0
    hombres = 0
    ani= []
    baby_chances = 0
    for i in integrantes:
        if isinstance(i, Persona):
            if i.genero == "F":
                mujeres+=1
                Mu.append(i)
            else:
                Hom.append(i)
        elif isinstance(i, Animal):
            animales+=1
            ani.append(i)
    if mujeres == 0 or mujeres == len(integrantes):
        if animales == 0:
            for i in integrantes:
                if isinstance(i, Persona):
                    i.moralidad +=random.randrange(-5,5)
            return []
        else:
            mujeres = animales
        #what if only male and animals?
    if hombres != 0:
        hombres = len(integrantes) - mujeres - animales
    if len(Hom) < len(Mu):
        Hom += ani
    else:
        Mu += ani
    mujer: Persona
    pregnant:dict = {}
    for i in Hom:
        Intentos[i] =  calcular_intentos(i)
    if mujeres >= 1:
        for mujer in Mu:
            if not isinstance(mujer, Animal):
                if mujer.oficio != 'Matriarca':
                    fertilidad = fertilidad_por_edad_f[int(mujer.edad)]
                else:
                    fertilidad = 100
                if mujer.personalidad["Secundaria"] != None:
                    if "Charming" in mujer.personalidad["Secundaria"]:
                        fertilidad += random.randrange(3,13)
            else:
                fertilidad= random.randrange(5,15)
            for npc in Hom:
                if Intentos[npc] > 0 and creampie(npc, fertilidad):
                    pregnant[mujer] = npc 
    return pregnant
def encunetra_antepasados(Perso: Persona):
    vistos=[]
    while Perso.padre != None and Perso.padre not in vistos:
        for i in [Perso.padre,Perso.madre]:
            if i not in vistos:
                vistos.append(i)
                visto = encunetra_antepasados(i) 
            for i in visto:
                if i not in vistos:
                    vistos.append(i)
    return vistos
def get_personalitys(Perso: Persona):
    principal = Perso.personalidad["Principal"]
    secundaria = Perso.personalidad["Secundaria"]
    return [principal, secundaria]
def enuentra_familia(nommbre_f):
    i: Familia
    for i in Familias:
        if i.nombre_familia == nommbre_f:
            return i
def born(pregnant:dict):
    def sexo(dad):
            name = random_name(random.randrange(3,8))
            dad:Persona = dad
            gender = random.choice(['M', 'F'])
            if mom.familia != dad.familia:
                mom_f:Familia = mom.familia
                dad_f:Familia = dad.familia
                if mom_f.funcionamiento != dad_f.funcionamiento:
                    f = random.choice([mom_f, dad_f])
                    if f == mom_f:
                        not_f = dad_f
                    else:
                        not_f = mom_f
                else:
                    if mom_f.funcionamiento == 'P':
                        f = dad_f
                        not_f = mom_f
                    elif mom_f.funcionamiento == 'M':
                        f = mom_f
                        not_f = dad_f
                if f.funcionamiento == 'P':
                    if gender == 'M':
                        son_f = f
                    else:
                        son_f = not_f
                else:
                    if gender == 'F':
                        son_f = f
                    else:
                        son_f = not_f
            else:
                son_f = mom.familia
            kid = Persona(name, son_f, str(0), gender, None, None, mom, dad)
            son_f.add(kid)
    galls = pregnant.keys()
    for i in galls:
        mom:Persona = i
        if isinstance(pregnant[i],Persona) !=  True:
            for b in pregnant[i]:
                sexo(b)
        else:
            sexo(pregnant[i])
    
