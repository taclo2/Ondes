
#Données à partir de la littérature
frequence_th1 = [345, 1033, 1820, 2041, 3240, 3835]
frequence_th2 = [263, 362, 585, 697, 775, 990]

#Données expérimentatles
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