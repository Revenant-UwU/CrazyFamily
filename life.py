from creador import *
import time
''''
All npc can do 4 actions per month.
-eat
-talk
-love
'''
turn = 0
month = ''
Months = ('Vasant','Moonson', 'Sharad rtu', 'Saedee')
class lugar:
    def __init__(self, nombre):
        self.sweet_text:str = ''
        self.acciones = ['talk', 'move']
        self.nombre = nombre
        self.personas = []
    def Actions(self, persona:Persona):
        persona:Persona
        if persona.estomago[0] <30 or persona.estomago[0] <30:
            pass #hay que poner a donde van dependindo de su rol
        if persona in NPC_vivos:
            if persona.estomago[0] <30 or persona.estomago[0] <30:
                accion = 'eat'
            else:
                accion = random.choice(self.acciones)
        else:
            accion = 'rot'
        if accion == 'talk':
            print(f'{persona} talked, they said this is their stomac: {persona.estomago}')
        if accion == "rot":
            print(persona, ' is rotting in place')
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
            if persona.estomago[0] <30 or persona.estomago[0] <30:
                if self.comida[0] > 0 and self.comida[1] >0:
                    accion = 'eat'
            else:
                accion = super().Actions(persona)
        if accion == 'eat':
            for i in [0,1]: persona.estomago[i] += random.randrange(22,35)
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
    print(f'{persona}, leaved {salida}, and arrived to {llegada}')
def r_where_to_move(persona:Persona, salida:lugar):
    lug = [] + todos_lugares
    lug.remove(salida)
    res = random.choice(lug)
    move(persona, salida, res)


def run_main(years:int):
    for Year in range(years):
        for Trun in range(4):
            month = Months[Trun]
            if NPC_vivos == []:
                for i in range(random.randrange(1,3)): 
                    print('\t'*random.randrange(0,3),'\033[31mall are dead\033[0m '*(Trun+1*Year))
                    time.sleep(1/(Trun+1*Year))
            else:
                print('\n', '-'*60, '\n')
                print('\t', month, str(Year+1), '\n \n')
                for i in todos_lugares:
                    if isinstance(i,casa):
                        for c in [0,1]: i.comida[c] += 1
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
lugares = {"Casas":[], "Escuela":  esc}
todos_lugares = [esc]
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
            b.add_p(c)
    print(lugares)
    for i in lugares['Casas']:
        print(i.show())
    run_main(30)
