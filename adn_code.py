import random
from creador import perosnalidades_p, perosnalidades_s
genotipos = {
    "Generous":    ['T', '_','T', 'S'],
    "Brave":       ['F', '_', 'F'],
    "Honest":      ["T",'T', "M"],
    "Greedy":      ["S", 'F','M'],
    "Cowardly":    ['T', 'M', '_', 'M'],
    "Manipulative":['M', 'S', 'M']
}
perso = list(genotipos.keys())

class ADN:  
    def __init__(self, name1 = None, name2= None, max_shift=None, lore = None):
        """
        First 16 lines of geneome should come from parents
        tre foro
        """
        if lore != None:
            if len(lore) > 16:
                error = f"lore: {lore} can't be over 16 on leng"
                raise ValueError(error) 
        self.name1 = name1
        self.name2 = name2
        if name1 == None or name2 == None:
            self.base1 = []
            self.base2 = []
            if lore !=None:
                genes= deconstusct(lore)
                print(genes)
                if len(genes) > 1:
                    name1 = genes[0][0]
                    name2 = genes[0][1]
                else:
                    name1= genes[0]
                    name2= genes[1]
                self.base1 = genotipos[name1][:]
                self.base2 = genotipos[name2][:]
                self.construct(name1,name2, None, lore)

        else:
            self.base1 = genotipos[name1][:]
            self.base2 = genotipos[name2][:]
            self.construct(name1, name2, max_shift, lore)
    def construct(self, name1 = None, name2= None, max_shift=None, lore = None):
        if lore != None:
            l = random.choice(lore)
            p = random.choice([self.base1,self.base2])
            s = [l] + p
            if p == self.base1:
                self.base1 = s
            else:
                self.base2 = s

        self.max_shift = (len(self.base1) + len(self.base2)) if max_shift is None else max_shift
        self.b_a = None
        error = 0
        while self.b_a == None:
            self.alignments = self.find_alignments()
            self.b_a = self.best_alignment()
            if self.b_a == None:
                error += 1
                self.name1 = name2
                self.name2 = name1
                self.base1 = genotipos[name2][:]
                self.base2 = genotipos[name1][:]
            if error == 2:
                self.name1 = name2
                self.name2 = name1
                self.base1 = genotipos[name2][:]
                self.base2 = genotipos[name1][:]
                self.base2 = ['_'] + self.base2
            if error == 3:
                raise TypeError
        self.best = self.b_a[0]
        self.best_to_base()
        self.genome = self.best["sequence_raw"]
        if lore != None:
            s = []
            for i in range(16):
                s.append(random.choice(lore))
            self.genome = s +['|'] +self.genome
    def ADN_is_compatible(self, a, b):
        if a == '_' or b == '_':
            return True
        reglas = {"M": ["T"], "F": ["S"], "S": ["F"], "T": ["M"]}
        return b in reglas.get(a, [])
    def pad_equal(self, s1, s2):
        a = s1[:]
        b = s2[:]
        if len(a) < len(b):
            a += ['_'] * (len(b) - len(a))
        elif len(b) < len(a):
            b += ['_'] * (len(a) - len(b))
        return a, b
    def combine_if_compatible(self, s1, s2):
        out = []
        for x, y in zip(s1, s2):
            if not self.ADN_is_compatible(x, y):
                return None  # incompatible para esta alineación
            out.append(x if x != '_' else y)
        return out
    def find_alignments(self):
        results = []
        for shift in range(self.max_shift + 1):
            shifted2 = ['_'] * shift + self.base2[:]
            a1, a2 = self.pad_equal(self.base1, shifted2)
            combined = self.combine_if_compatible(a1, a2)
            if combined is None:
                results.append({
                    "shift": shift,
                    "compatible": False,
                    "sequence_raw": [],
                    "length_raw": 0,
                    "aligned_geno1": a1,
                    "aligned_geno2": a2
                })
            else:
                results.append({
                    "shift": shift,
                    "compatible": True,
                    "sequence_raw": combined,
                    "length_raw": len(combined),
                    "aligned_geno1": a1,
                    "aligned_geno2": a2
                })
        return results
    def any_compatible(self):
        return any(r["compatible"] for r in self.alignments)

    def best_alignment(self):
        compatibles = [r for r in self.alignments if r["compatible"]]
        if not compatibles:
            return None
        # elegir la compatible con menor length_trimmed (si empata, menor shift)
        compatibles.sort(key=lambda r: (r["length_raw"], r["shift"]))
        return compatibles
    def best_to_base(self):
        self.base1 = self.best['aligned_geno1']
        self.base2 = self.best['aligned_geno2']
        self.lenght = self.best['length_raw']
    def __repr__(self):
        return f'{self.base1} \n {self.base2}'

def match_gene(seq, gene):
    n, m = len(seq), len(gene)
    for i in range(n - m + 1):  # recorrer ventanas
        window = seq[i:i+m]
        if all(a == b or a == "_" or b == "_" for a, b in zip(window, gene)):
            return True  # encontrado en posición i
    return False  # no encontrado
def find_genes(adn):
    '''will only search on the last 20 lines of genome'''
    genes = []
    keys= adn_dic.keys()
    keys = list(keys)
    if isinstance(adn,ADN):
        b:list = adn.genome
    else:
        b:list = adn
    for i in range(len(adn_dic)):
        if match_gene(b, keys[i]):
            genes.append(adn_dic[keys[i]])
    return genes
def deconstusct(adn:ADN):
    def count(gen:ADN):
        if isinstance(gen, ADN):
            gen = gen.genome
        else:
            gen = gen
        M = 0
        T = 0
        F = 0
        S = 0
        for i in gen:
            if i == 'M':
                M += 1
            if i == 'T':
                T +=1
            if i == 'F':
                F += 1
            if i == 'S':
                S += 1
        l = {'Mental': M, 'Sexual': S, 'Fisical':F, 'Talent':T}
        return l
    perso_p = []
    p_s = []
    genes = find_genes(adn)
    for i in genes:
        if i in perosnalidades_p:
            perso_p.append(i)
        if i in perosnalidades_s_value:
            p_s.append(i)
    perso_p = random.sample(perso_p, k=2)
    if len(p_s) > 3:
        m =[]
        f= []
        s= []
        t= []
        lis = [mental, fisca, sexual, talent]
        for i in p_s:
            for b in range(len(lis)):
                if i in lis[b]:
                    if  b == 0:
                        m.append(i)
                    if b ==1:
                        f.append(i)
                    if b == 2:
                        s.append(i)
                    if b == 3:
                        t.append(i)
        cunt = count(adn)
        pesos = [cunt[c] for c in cunt]
        seleccion = random.choices([m,s,f,t], weights=pesos, k=3)
        final = []
        for i in seleccion:
            if i != []:
                b = random.choice(i)
                if b != []:
                    lmao = 0
                    while b in final and lmao < 3:
                        b = random.choice(i)
                        lmao += 1
                    if  b not in final:
                        final.append(b)
        p_s = final
    return perso_p, p_s
def create_lore(adn_m:ADN, adn_f: ADN)-> list:     
    """Create psuedo genome for lore"""
    void_adn = ADN()
    lower = random.choice([adn_m,adn_f])
    if lower == adn_m:
        upper = adn_f
    else:
        upper= adn_m
    void_adn.base1 = upper.base1
    void_adn.base2 = lower.base2
    void_adn.construct()
    lore:list =void_adn.genome
    while len(lore) > 20:
        lore.remove(random.choice(lore))
    return lore
fun = []
# Ejemplo: generar todas las parejas (sin duplicados A+B y B+A)
dd= 0
d = 0
c = []
while len(fun) < 41:
    #print(fun)
    for i in range(len(perso)):
        for j in range(i+1, len(perso)):
            adn = ADN(perso[i], perso[j], 12)
            b = 0
            while adn.best in fun:
                b += 1
                if b > len(adn.b_a):
                    raise IndexError
                adn.best = adn.b_a[b]

            fun.append(adn.best)
mental = perosnalidades_s["Mental"]
fisca = perosnalidades_s["Fisical"]
sexual = perosnalidades_s["Sexual"]
talent = perosnalidades_s["Talent"]
perosnalidades_s_value = [] + mental + fisca + sexual + talent
per = [] + mental + fisca + sexual + talent 

b=0
adn_dic = {}
for i in fun:
    try:
        c = tuple(i['sequence_raw'])
        adn_dic[c] = f'{per[b]}'
        if b != len(per):
            b += 1
        else:
                break
    except:
        pass
genotipos_t = {k: tuple(v) for k, v in genotipos.items()}
invertido = {v: k for k, v in genotipos_t.items()}
adn_dic =  invertido | adn_dic    
