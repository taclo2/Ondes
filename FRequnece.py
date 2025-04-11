
#Données à partir du guide d'achat
frequence_th1 = [345, 1033, 1820, 2041, 3240, 3835]

#Données à partir d'une étude
frequence_th2 = [263, 362, 585, 697, 775, 990]

#Données expérimentales
frequence_exp = [329.37, 484.50, 767.14, 941.16, 1027.50, 1345.50]


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

#Ratio des modes n et m
def ratios_modes():
    modes = []

    for n1 in range(2, 11, 2):
        for m1 in range(2, 11, 2):
            if n1 > m1:  # on impose n1 <= m1 pour éviter les doublons
                continue
            num = n1**2 + m1**2
            for n2 in range(2, 11, 2):
                for m2 in range(2, 11, 2):
                    if n2 > m2: 
                        continue
                    if n1 == n2 and m1 == m2 :
                        continue
                    
                    denom = n2**2 + m2**2
                    ratio = round(num / denom, 4)
                    modes.append({((n1, m1), (n2, m2)): ratio})

    return modes

print(ratios_modes())
