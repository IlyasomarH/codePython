def calcul_moyenne(liste):
    
    try:
        somme=0
        taille=0
        
        if taille==0:
            return 0
        else:
            for element in liste:
                somme= somme+element
            return somme/taille
    except:
        print("vous devez saisir une liste valide")
    

liste=[12,9,15,16]

# moyenne=calcul_moyenne(liste)

# print("la moyenne est ", moyenne)



# Exercice 2

def compte_mots(phrase):
    mots=phrase.split()
    return len(mots)





chaine="Ilyas"

# print(chaine[-6])

# nombre_mot=compte_mots(phrase)

# print("le nombre de mot sont :", nombre_mot)



# exercice 3

def inverse_chaine(chaine):
    
    chaineIverse=[]
    lastchaine=""
    

    for i in range(len(chaine)+1):
        if i==0:
            continue
        else:
            
            chaineIverse.append(chaine[-i])
    for element in chaineIverse:
        lastchaine +=element
        
    return lastchaine



chaineIverse=inverse_chaine(chaine)

print(chaineIverse)




