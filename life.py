from creador import *
import time
''''
Ciudades, Familias, Guerras, Bancos.

'''
turn = 0
month = ''
Months = ('\033[32mVasant\033[0m','\033[34mMoonson\033[0m', '\033[33mSharad\033[0m', '\033[36mSaedee\033[0m')
class lugar:
    ''''
    Base from all the places to be. It has a name and stores acctions the person may take.
    '''
    def __init__(self, nombre):
        self.sweet_text:str = ''
        self.acciones = ['talk', 'move']
        self.nombre = nombre
        self.personas = []
    def Actions(self, persona:Persona):
        persona:Persona
        accion = ''
        if persona.estomago[0] <30 or persona.estomago[0] <30 and persona.healt > 0:
            pass #hay que poner a donde van dependindo de su rol
        if persona in NPC_vivos:
            if persona.estomago[0] <30 or persona.estomago[0] <30:
                if persona.oficio not in [oficios.Cazador, oficios.Buzcador_a] and not isinstance(self, casa):
                    print('\033[35mDue to  hunger or thirst\033[0m', persona, ' \033[35mis going back home\033[0m')
                    move(persona, self, persona_home_location(persona))
                elif persona.oficio is oficios.Buzcador_a:
                    popop= random.choice(move_to_location(pozo))
                    if popop is not self:
                        move(persona, self, popop)
            else:
                accion = random.choice(self.acciones)
        else:
            accion = 'rot'
        if accion == 'talk':
            print(f'{persona} talked, they said this is their stomac: {persona.estomago}')
        if accion == "rot":
            print('\033[31m',persona, 'is rotting in place\033[0m')
            for i in self.personas:
                i.healt -= random.randrange(1,3)
        if accion == 'move':
            r_where_to_move(persona, self)
        return accion
    def contar(self):
        return len(self.personas)
    def show(self):
        return self.personas
    def __repr__(self):
        return f'{self.nombre}: {self.sweet_text}'
    def add_p(self, person:Persona):
        if person not in self.personas:
            self.personas.append(person)
        else:
            raise KeyError(f'{person} alredy in {self}')
    def remove_p(self, person:Persona):
        if person in self.personas:
            self.personas.remove(person)
        else:
            raise KeyError(f'{person} not in {self.personas}')
class casa(lugar):
    def __init__(self, nombre, familia:Familia):
        super().__init__(nombre)
        new_actions = ['eat']
        self.food = True
        self.acciones = new_actions + self.acciones
        self.sweet_text = 'Great house!'
        self.familia = familia
        comida = 10
        agua = 10
        self.comida = [comida, agua]
    def Actions(self, persona:Persona):
        accion = 'talk'
        if self.comida[0] == 0 or self.comida[1] == 0 :
            if self.food:
                print(f'{self} ran out of food')
                self.food = False
            if 'eat' in self.acciones:
                self.acciones.remove('eat')
        else:
            self.food = True
            if 'eat' not in self.acciones:
                self.acciones.append('eat')
        if persona in NPC_vivos:
            if self.comida[1] < len(self.familia.miembros) + 2 and persona.oficio not in [oficios.Patriarca, oficios.Matriarca, oficios.Buzcador_a]:
                Okydo = False
                if persona.familia.count_ofices(oficios.Buzcador_a) < persona.familia.count_ofices(oficios.Cazador):
                    Okydo = True
                if self.comida[1] < (len(self.familia.miembros)//2) - 1:
                    if persona.edad >=10:
                        if persona.oficio == oficios.Cazador and Okydo:
                            persona.oficio = oficios.Buzcador_a
                        elif persona.oficio != oficios.Cazador:
                            persona.oficio = oficios.Buzcador_a
                if persona.edad >= 18:
                    if persona.oficio == oficios.Cazador and Okydo:
                        persona.oficio = oficios.Buzcador_a
                    elif persona.oficio != oficios.Cazador:
                        persona.oficio = oficios.Buzcador_a
            if persona.estomago[0] <30 or persona.estomago[0] <30:
                if self.comida[0] > 0 and self.comida[1] >0:
                    accion = 'eat'
            else:
                accion = super().Actions(persona)
        if accion == 'eat':
            for i in [0,1]: persona.estomago[i] += random.randrange(30,45)
            for i in [0,1]: self.comida[i] -= 1
            print(f'{persona} esta comiendo')
class escuela(lugar):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.sweet_text = 'Study place'
        self.profesors = []
        self.students = []
        self.sort()
    def sort(self):
        for i in [self.profesors, self.students]:
            for b in i:
                if b not in self.personas:
                    i.remove(b)
        for i in self.personas:
            i:Persona
            if i.edad > 19:
                self.profesors.append(i)
            else:
                self.students.append(i)
class pozo(lugar):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.water:float = 20.0
        self.max_water:float = 60.0
        self.water_regeneration:float = 1.0
        self.posion = False
        self.sweet_text = ''
        self.acciones = ['take water', 'posion water'] + self.acciones
    def Actions(self, persona):
        accion = 'talk'
        if self.posion and self.water > 0:
            persona.healt -= self.water - 0.4*abs(persona.moralidad - 100)
            dmg = self.water - 0.4*abs(persona.moralidad - 100)
            print('\t', persona, '\033[32m drank potioned water and recived :\033[0m \033[32m', dmg, '\033[0m\033[32mamout of dmg \033[0m' )
        if persona in NPC_vivos:
            if self.water >= self.water*0.70:
                if random.random():
                    persona.estomago[1] += 15
                    self.water -= random.choice([0.8, 1.0])
                    print('\033[35m seing the fountian full', persona, '\033[35m took a sip\033[0m' )
            if persona.oficio is oficios.Buzcador_a and persona_home_location(persona).comida[1] < len(persona.familia.miembros):
                if 'Cowardly' in persona.personalidad['Principal']:
                    if persona.estomago[1] <50:
                        if self.water > 0:
                            n = 0
                            if 'Greedy' in persona.personalidad['Principal']:
                                n = 1
                            self.water -= 1.0 + n
                            persona.estomago[1] += 25 + 25*n
                elif 'Greedy' in persona.personalidad['Principal']:
                    if persona.estomago[1] <50:
                        if self.water > 0:
                            self.water -= 1.0
                            persona.estomago[1] += 25
                if persona.estomago[1] <40 and 'Greedy' not in persona.personalidad['Principal'] :
                    if self.water > 0:
                        self.water -= 1.0
                        persona.estomago[1] += 25
                if self.water > 1.0:
                    home = persona_home_location(persona)
                    min_t = len(persona.familia.miembros)
                    if self.water >= float(min_t):
                        home.comida[1] += min_t + 1
                        self.water -= min_t + random.choice([0,1.0,-1.0])
                    else:
                        home.comida[1] += self.water
                        self.water = random.choice([0,1.0,-0.5]) 
            
                    print(persona, '\033[35m under his duty took water home\033[0m' )
            else:
                super().Actions(persona)
        else:
            accion = super().Actions(persona)
            if accion == 'rot' and random.randrange(0,5) == 2 and self.posion == False:
                self.posion = True
                print('\n\t\033[32m', '-*'*60)
                print(persona, '\033[37m body posined the water')
                print('\n\t\033[32m', '-*'*60, '\033[0m')
    def changes_per_seson(self):
        m = Months[month]
        if m ==  Months[0]:
            self.water_regeneration += 5.5
        elif m == Months[1]:
            self.water += self.water/4
            self.water_regeneration += 5.5
        elif m == Months[2]:
            self.water = -abs(self.water/10)
            self.water_regeneration -= 11.0
        elif m == Months[3]:
            self.water +=0.5
            self.water_regeneration += 3.0
            self.max_water += random.choice([1.5, -1.8])
        if random.randrange(0,100) >99:
            self.posion = True
    def refil_self(self):
        self.changes_per_seson()
        if self.water > self.max_water:
            self.water -= self.water/10
            if random.randrange(0,100) >99:
                self.posion = True
        else:
            if self.water <0:
                self.water = 0.0
                if random.random() == 1:
                    self.posion = False
            self.water += self.water_regeneration
    def __repr__(self):
        return f"{self.nombre}, water: {self.water}, m :{self.max_water}, water regen:{self.water_regeneration},\n poison: {self.posion}, {self.personas}"
    
def move(persona:Persona, salida:lugar, llegada:lugar):
    if persona not in salida.personas :
        raise KeyError
    if persona in llegada.personas:
        raise KeyError
    salida.remove_p(persona)
    llegada.add_p(persona)
    if isinstance(salida, escuela):
        salida.sort()
    elif isinstance(llegada, escuela):
        llegada.sort()
    print(f'{persona}, \033[33mleaved {salida} \033[0m, and arrived to \033[33m{llegada}\033[0m')
def r_where_to_move(persona:Persona, salida:lugar):
    lug = [] + todos_lugares
    lug.remove(salida)
    res = random.choice(lug)
    move(persona, salida, res)
def move_to_location(clase) ->list:
    b = []
    for i in todos_lugares:
        if isinstance(i,clase):
            b.append(i)
    if b == []:
        raise IndexError('No ', clase, ' found in the list of places here : \n', todos_lugares)
    else:
        return b
def persona_home_location(persona:Persona) -> casa :
    for i in lugares['Casas']:
        if i.familia == persona.familia:
            return i
def run_main(years:int):
    for Year in range(years):
        for Trun in range(4):
            global month
            month = Trun
            #print('\t\033[4m', Months[month], '\033[0m\n \n')
            if NPC_vivos == []:
                for i in range(random.randrange(1,3)): 
                    print('\t'*random.randrange(0,3),'\033[31mall are dead\033[0m '*(Trun+1*Year))
                    time.sleep(1/(Trun+1*Year))
            else:
                print('\n', '-'*60, '\n')
                print('\t\033[4m', Months[month], str(Year+1), '\033[0m\n \n')
                for i in todos_lugares:
                    if isinstance(i,casa):
                        for c in [0,1]: i.comida[c] += 3
                    if isinstance(i,pozo):
                        i.refil_self()
                        print(i)
                    for b in i.personas:
                        if b in NPC_vivos:
                            b.muerte()
                        i.Actions(b)
                if Trun == 3:
                    for i in NPC_vivos:
                        i.edad += 1
                    print('Vivos', NPC_vivos)
                    print('Muertos', NPC_muertos)
            input()



esc = escuela(random_name(3)+ ''+ random_name(5))
#esc =  escuela('Saint Boniface')
lugares = {"Casas":[], "Escuela":  esc, "Pozos": pozo('Fuente central')}
todos_lugares = [esc] + [lugares['Pozos']]
month = 0
if __name__ == '__main__':
    #Uno =  Familia('Neri')
    #dos = Familia('Valentin')
    #Jorge = Persona('Jorge', Uno, 20, 'M', {'Principal':['Generous', 'Honest'], 'Secundaria':[]}, 'Estudiante', None, None, None)
    #Anita =  Persona('Anita', dos, 25, 'F', {'Principal':['Generous', 'Honest'], 'Secundaria':['Charming']} ,'Estudiante', None, None, None )
    #Kylian= Animal('Kilian da dog')
    #for i in range(10):
   #     print('we had s word: ', i, ' times')
    #    print(SEXO([Anita, Jorge]))
    #Uno.add(Jorge)
    #dos.add(Anita)
    
    #b = casa(Uno.nombre_familia, Uno)
    #c = casa(dos.nombre_familia, dos)
    for i in ['ll','ghjg', 'iooiu']:
        i = Familia(i)
        i.constructor_familia()
        b = casa(i.nombre_familia, i)
        lugares['Casas'].append(b)
        todos_lugares.append(b) #Append las casas a la lista de lugares a mover
        for c in i.miembros:
            c.edad += random.choice([10, 20, 30])
            b.add_p(c)
    print(lugares)
    for i in lugares['Casas']:
        print(i.show())
    run_main(10)
