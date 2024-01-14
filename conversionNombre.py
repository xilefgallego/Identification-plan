NOMBRES_EN_LETTRES = {
    "zéro"	:	0,
    "un "	:	1,
    "une"	:	1,
    "deux"	:	2,
    "de"    :   2,
    "trois"	:	3,
    "quatre"	:	4,
    "cinq"	:	5,
    "six"	:	6,
    "sept"	:	7,
    "cette" :   7,
    "huit"	:	8,
    "set it"    :   8,
    "neuf"	:	9,
                
    "dix"	:	10,
    "onze"	:	11,
    "douze"	:	12,
    "treize"	:	13,
    "quatorze"	:	14,
    "quinze"	:	15,
    "seize"	:	16,
    "dix-sept"	:	17,
    "dix-huit"	:	18,
    "dix-neuf"	:	19,
                
    "vingt"	:	20,
    "vingt et un"	:	21,
    "vingt-deux"	:	22,
    "vingt-trois"	:	23,
    "vingt-quatre"	:	24,
    "vingt-cinq"	:	25,
    "vingt-six"	:	26,
    "vingt-sept"	:	27,
    "vingt-huit"	:	28,
    "vingt-neuf"	:	29,
                
    "trente"	:	30,
    "trente et un"  :   31,
    "trente-deux"	:	32,
    "trente-trois"	:	33,
    "trente-quatre"	:	34,
    "trente-cinq"	:	35,
    "trente-six"	:	36,
    "trente-sept"	:	37,
    "trente-huit"	:	38,
    "trente-neuf"	:	39,

    "quarante"	:	40,
    "cinquante"	:	50,
    "soixante"	:	60,
    "soixante-dix"	:	70,
    "quatre-vingts"	:	80,
    "quatre-vingt-dix"	:	90,
                
    "cent"	:	100,
}

# converti les mots en chiffres
def lettres_en_chiffres_francais(mot):
    return NOMBRES_EN_LETTRES.get(mot, None)

cTot=0
cTrv=0

# identification de la prise
def idPrise(ligne):
    # on cherche trois nombres
    # soit n le nombre de nombres trouvés
    n = 0
    pos = []
    
    ## SOLUTION 1
    # recherche progressive des nombres dans la ligne
    # for i in ligne:
    #     if(" " in i):
    #         #tester si ce qui suit est un nombre
    #         if ():
    #             n+=1

    ## SOLUTION 2
    # On cherche tous les nombres possibles dans la ligne
    # for nombre in NOMBRES_EN_LETTRES.keys():
    #     # Si on trouve un nombre dans la ligne
    #     if (ligne.find(nombre) != -1):
    #         tup = (ligne.find(nombre), NOMBRES_EN_LETTRES.get(nombre))
    #         pos.append(tup) 
    #         n+=1
    #         #print("position "+ str(ligne.find(nombre)))
    # print (pos)
    # if (n == 3):
    #     pos.sort() # key=lambda a: a[1]
    #     return "S"+str(pos[0][1])+"P"+str(pos[1][1])+"p"+str(pos[2][1])
    # else:
    #     return "Erreur nombres trouves : " + str(n)

    ## SOLUTION 3
    # recherche progressive des nombres dans la ligne mot par mot
    mots = ligne.split()
    N = []

    i = 0
    while i < len(mots):
        mot = mots[i]
        nombre = lettres_en_chiffres_francais(mot)

        if nombre is not None:
            if i + 1 < len(mots) and mots[i + 1] in NOMBRES_EN_LETTRES: # trente deux
                nombre_suivant = lettres_en_chiffres_francais(mots[i + 1])
                nombre += nombre_suivant
                i += 1
            elif i + 2 < len(mots) and mots[i+1] == "et" and mots[i+2] == "un": # trente et un
                nombre += 1
                i += 2

            N.append(nombre)

        i += 1
    
    if (len(N)==3):
         return "S"+str(N[0])+"P"+str(N[1])+"p"+str(N[2])
    else:
        return "Erreur nombres trouves : " + str(len(N)) + " " + str(N)
