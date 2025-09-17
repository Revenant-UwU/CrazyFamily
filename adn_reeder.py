from adn_code import *


keys= adn_dic.keys()
adn_p = ADN('Brave', "Generous")
adn_s = ADN("Generous", "Manipulative", 3, adn_p.genome)
adn_c = ADN("Cowardly", "Manipulative", 3, create_lore(adn_p, adn_s))
adn_1 = ADN('Brave', "Generous")
adn_2 = ADN(None,None,None, create_lore(adn_1, adn_1))
adn_3 = ADN(None, None, None,  create_lore(adn_1, adn_2))
adn_4 = ADN(None, None, None,  create_lore(adn_2, adn_3))
adn_5 = ADN(None, None, None,  create_lore(adn_3, adn_4))
adn_6 = ADN(None, None, None,  create_lore(adn_4, adn_4))
r = 0
iii =[adn_1, adn_2,adn_3, adn_4, adn_5]
iv = []
with open("resultados4.txt", "w", encoding='utf-8') as f:
    for i in range(len(iii)):
        r += 1
        print("-"*60, file=f)
        print (r,file=f)
        if r ==2:
            print(f'son of 1 wiht itself',file=f )
        elif r == 5:
            print('son of 4 wiht 4', file=f)
        else:
            print(f'son of {i} and {r}',file=f)
        print('', file=f)
        print('ADN: ',file=f)
        print (f'   {iii[i]}',file=f)   
        print('', file=f)
        print('Genome: ',file=f)
        print (f'   {iii[i].genome}',file=f)   
        print('', file=f)
        print('Potential genes: ',file=f) 
        print(f'    {find_genes(iii[i])}',file=f)
        print('', file=f)
        print('Selected genes: ',file=f) 
        print(f'    {deconstusct(iii[i])}',file=f)
        #if i+1 < len(iii):
            #print(create_lore(iii[i], iii[i+1]))
        #else:
            #print(create_lore(iii[0], iii[i]))
