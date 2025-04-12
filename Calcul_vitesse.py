#Écrire le premier mode possible selon la géométrie
n1 = 2
m1 = 2

#Écrire le nombre de fréquence à comparer
nb_f = 3

#Écrire la longueur de la plaque en mètre
L = 0.24

#Données à partir du guide d'achat
frequence_th1 = [345, 1033, 1820, 2041, 3240, 3835]

#Données à partir d'une étude
frequence_th2 = [263, 362, 585, 697, 775, 990]

#Données expérimentales
frequence_exp = [329.37, 484.50, 767.14, 941.16, 1027.50, 1345.50]


#Division des fréquences consécutives mises au carré et multipliées par 2L
def ratio_frequence(frequences):
    if len(frequences) < 2:
        raise ValueError("La liste doit contenir au moins deux fréquences.")
    
    #Division des frequence consécutive
    ratios = []
   
    for i in range(len(frequences) - 1):
        ratio = (frequences[i] / frequences[i + 1])
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


print()
print("Les valeurs possibles au numérateur :", num(n1, m1, nb_f))
print()
print("Les valeurs possibles au dénominateur :", denum(n1, m1, nb_f))


#Effectuer la division des modes consécutifs
def division_mode(n1, m1, nb_f):
    numerateur = num(n1, m1, nb_f)
    denominateur = denum(n1, m1, nb_f)
    division = {}

    for clé_num, valeur_num in numerateur.items():
        for clé_denum, valeur_denum in denominateur.items():
            
            n_num, m_num = clé_num
            n_denum, m_denum = clé_denum

            #Passer les valeurs égales
            if clé_num == clé_denum:
                continue
            
            #Considérer uniquement 2 mode consécutif
            if n_denum > n_num + 2 or m_denum > m_num + 2:
                continue

            #Enlever les valeurs avec un numérateur supérieur
            if (n_num + m_num) > (n_denum + m_denum):
                continue

            #Enlever les valeurs où n_denum est plus petit que n_num
            #Le mode au dénominateur est toujours le plus grand
            if n_denum < n_num:
                continue

            calcul = valeur_num / valeur_denum
            division[(clé_num, clé_denum)] = calcul

    return division

print()
print("Les valeurs de division des modes :", division_mode(n1, m1, nb_f))
print()

#Calcul de vitesse des ondes
#Fin du code par manque d'idées et d'inspiration


"""
Pour la suite nous allons choisir le ratio de modes le plus proche de la valeur de la première fréquence
Pour la deuxième fréquence, nous prenons le prochain mode mode consécutif ayant une valeur similaire

Valeur des vitesses calculées :

J'assume que la première fréquence (329.37) est le premier mode pair soit (n=2, m=2), donc 
v1 = (329.37*0.48)/(n**2 + m**2)**(1/2) = 55.90 m/s

Pour la deuxième fréquence (484.50), j'assume que le mode est (n=2, m=4). Ainsi, la troisième fréquence (767.14) serait le mode (n=4, m=4)
v2 = (484.50*0.48)/(n**2 + m**2)**(1/2) =  52.00 m/s
v3 = (767.14*0.48)/(n**2 + m**2)**(1/2) =  65.09 m/s

La quatrième fréquence (941.16) pourrait alors être le mode (n=4 , m=6)
v4 = (941.16*0.48)/(n**2 + m**2)**(1/2) =  62,64 m/s

"""