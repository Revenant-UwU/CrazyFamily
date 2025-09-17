from creador import *
import unittest

class Test_name(unittest.TestCase):
    def test_name_lenght(self):
        for i in [3,4,5,6,7,8,9]:
            self.assertEqual(i, len(random_name(i)))
            #print(random_name(i))
    def test_name_on_list(self):
        nombre= ['Jacinto', 'Ramiro', 'Juan', 'Don', 'Javier', 'Jose']
        for i in ['Jacinto', 'Ramiro', 'Juan', 'Don']:
            new_nombre= name_not_in_list(i, nombre, 4, 6)
            self.assertAlmostEqual(len(new_nombre), 5,None, None, 2)
            self.assertIn(new_nombre, nombre)
    def test_persons_atributes(self):
        Marth = Persona("Marth", "Grand", "19", "M",  {"Principal": ["Brave", "Honest"], "Secundaria": ["Pedofile", "Albino"]}, "Crazy", None, None)
        Girlfriend = Persona("Grey", "Son", "18", "F",  {"Principal": ["Manipulative", "Honest"], "Secundaria": None}, "Crazy", None, None)
        Son = Persona("Kiddo", "Grand", "5", "M", None, None, Girlfriend, Marth)
        for Npc in [Marth, Girlfriend, Son]:
            NPC_vivos.append(Npc)
        BF = Pareja(Marth, None)
        GF = Pareja(Girlfriend, None)
        BF.pareja = GF
        GF.pareja = BF
        person: Persona
        self.assertEqual(sorted(NPC_vivos, key=lambda person: person.nombre), sorted([BF, GF, Son], key=lambda person: person.nombre))
        self.assertEqual(Marth.nombre, BF.nombre)
        self.assertEqual(BF, Son.padre)
        self.assertEqual(GF, Son.madre)
#    def test_morality(self):
#        Marth = Persona("Marth", "Grand", "19", "M",  {"Principal": ["Brave", "Honest"], "Secundaria": ["Pedofile", "Albino"]}, "Crazy", None, None)
#        Girlfriend = Persona("Grey", "Son", "18", "F",  {"Principal": ["Manipulative", "Honest"], "Secundaria": None}, "Crazy", None, None)
#        Son = Persona("Kiddo", "Grand", "5", "M", None, None, Girlfriend, Marth)
#        self.assertAlmostEqual(Marth.moralidad, 24, None, f'Expected is between 13 and 34, actual result: {Marth.moralidad}', 20)
#        self.assertEqual(Girlfriend.moralidad, 11,f'Expected is 11, actual result: {Girlfriend.moralidad}' )
#        self.assertEqual(Son.moralidad, 0,f'Expected is 0, actual result: {Son.moralidad}' )
    def test_SEXO(self):
        Marth = Persona("Marth", "Grand", "19", "M",  {"Principal": ["Brave", "Honest"], "Secundaria": ["Pedofile", "Albino"]}, "Crazy", None, None)
        Girlfriend = Persona("Grey", "Son", "18", "F",  {"Principal": ["Manipulative", "Honest"], "Secundaria": []}, "Crazy", None, None)
        Son = Persona("Kiddo", "Grand", "5", "F",  {"Principal": ["Greedy",  "Honest"], "Secundaria": ["Charming"]}, "None", Girlfriend, Marth)
        wild_dog= Animal("Wild Dog")
        for i in [[Marth, Girlfriend, Son, wild_dog], [Marth, wild_dog], [Girlfriend, Son, wild_dog], 
                  [ Girlfriend, wild_dog], [Marth, Son, wild_dog], [Marth, Son], [Marth, Girlfriend], [Girlfriend, Son],
                    [Marth, Girlfriend, Son]]:
            c = 0
            second_dic= {}
            lista= []
            for b in range(10):
                pregancy = SEXO(i)
                c += len(pregancy)
                for person in pregancy:
                    if person not in lista:
                        lista.append(person)
                        second_dic[person] = {pregancy[person]: 1}
                    else:
                        if pregancy[person] in second_dic[person]:
                            second_dic[person][pregancy[person]] += 1
                        else:
                            second_dic[person][pregancy[person]] = 1
                    if pregancy[person] not in lista:
                        lista.append(pregancy[person])
                        second_dic[pregancy[person]] = 1
                    else:
                        second_dic[pregancy[person]] += 1
            print('___________________________')
            print(f'this ppl had sex {i} , they had {c} pregnancies over 10 reunions')
            print('___________________________')
            print('')
            for i in second_dic:
                if isinstance(i, Persona) and i.genero == "F":
                    for b in second_dic[i]:
                        print(f'{i} got pregnat by {b}: {second_dic[i][b]} number of times')
                        print( "")
    def test_encuentra_padres(self):
        
        Girlfriend2 = Persona("Grey", "2", "18", "F",  {"Principal": ["Manipulative", "Honest"], "Secundaria": None}, "Crazy", None, None)
        Marth3 = Persona("Marth", "3", "19", "M",  {"Principal": ["Brave", "Honest"], "Secundaria": ["Pedofile", "Albino"]}, "Crazy", None, None)
        Girlfriend3 = Persona("Grey", "3", "18", "F",  {"Principal": ["Manipulative", "Honest"], "Secundaria": None}, "Crazy",None , None)
        Marth2 = Persona("Marth", "2", "19", "M",  {"Principal": ["Brave", "Honest"], "Secundaria": ["Pedofile", "Albino"]}, "Crazy", Marth3, Girlfriend3)
        Marth = Persona("Marth", "Grand", "19", "M",  {"Principal": ["Brave", "Honest"], "Secundaria": ["Pedofile", "Albino"]}, "Crazy", Marth2, Girlfriend2)
        Girlfriend = Persona("Grey", "Son", "18", "F",  {"Principal": ["Manipulative", "Honest"], "Secundaria": None}, "Crazy", Marth3, Girlfriend3)
        Son = Persona("Kiddo", "Grand", "5", "M", None, None, Girlfriend, Marth)
        print("______test encuentra padres_____")
        print(encunetra_antepasados(Son))
        print("______fin_________")
        
        
if __name__ ==  '__main__':
    unittest.main()