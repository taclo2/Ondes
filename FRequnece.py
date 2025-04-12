
#Données à partir du guide d'achat
frequence_th1 = [345, 1033, 1820, 2041, 3240, 3835]

#Données à partir d'une étude
frequence_th2 = [263, 362, 585, 697, 775, 990]

#Données expérimentales
frequence_exp = [329.37, 484.50, 767.14, 941.16, 1027.50, 1345.50]

#Division des fréquences consécutives
def ratio_frequence(frequences):
    #Division des frequence consécutive
    if len(frequences) < 2:
        raise ValueError("La liste doit contenir au moins deux fréquences.")
    ratios = []
   
    for i in range(len(frequences) - 1):
        ratio = frequences[i] / frequences[i + 1]
        ratios.append(ratio)
    return ratios


#Ratios 
ratios_th1 = ratio_frequence(frequence_th1)
ratios_th2 = ratio_frequence(frequence_th2)
ratios_exp = ratio_frequence(frequence_exp)


#Afficher les valeurs
print(ratios_th1)
print()
print(ratios_th2)
print()
print(ratios_exp)
print()



#Fonction des combinaisons de N et M
def combi_modes(n1, m1, nb_f):
    N = [(n1,)]
    M = [(m1,)]

    for i in range(nb_f):
        ajout_n = tuple()
        ajout_m = tuple()

        for n in N[i]:
            ajout_n += (n, n+2, n+2)

        for m in M[i]:
            ajout_m += (m+2, m, m+2)


        N.append(ajout_n)
        M.append(ajout_m)

    return N, M


#Calcul des valeurs possibles au numérateur
def num(n1, m1, nb_f):
    N, M = combi_modes(n1, m1, nb_f)
    longueur = len(N)
    mode_num = {}

    #Pour les indices de la liste de N
    for i in range(longueur):
        longueur_tuple = len(N[i])

        #Pour les indices des tuples dans N
        for j in range(longueur_tuple):
            valeur_n = N[i][j]
            valeur_m = M[i][j]
            calcul = (valeur_m**2 + valeur_n**2)
            mode_num[(valeur_n, valeur_m)] = calcul

    #On élimine les doublons
    a = []
    b = []

    for clé, valeur in mode_num.items():
        if not valeur in a:
            a.append(valeur)

        else:
            b.append(clé)

    for clé in b:       
        del mode_num[clé]


    return mode_num


#Calcul des valeurs possibles au dénominateur
def denum(n1, m1, nb_f):

    #Prendre la liste des numérateurs et enlever le premier mode
    mode_denum = dict(list(num(n1, m1, nb_f).items())[1:])
    
    return mode_denum



print(combi_modes(2, 2, 2))
print()
print(num(2, 2, 2))
print()
print(denum(2, 2, 2))