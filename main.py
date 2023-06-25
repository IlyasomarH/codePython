# Exercice 1

# def calculerMoyenne(tab):
#     somme=0
#     taille_tab=0
  
#     try:    
#         for element in tab:
#             somme+=element
#             taille_tab+=1
#         if taille_tab==0:
#             return 0
#         else:
                
#             return somme/taille_tab
#     except:
#         print("saisi des nombres valide")
#         return "invalide"
       


# liste=[12,16,15]
# print('la moyenne est ' , calculerMoyenne("je suis "))





# Exercice 2


# def compte_mots(phrases):
#     mots=[]
#     compteur=0
#     mots=phrases.split("'")
    
    
#     for mot in mots:
#         compteur+=1

#     print("il y'a ", compteur , ' Mots, dans cette phrase ')


def compte_mots(phrases):
    pass
    # mots=[]
   
    # mots=phrases.split()

    # print("il y'a ",len(mots) , ' Mots, dans cette phrase ')
    
# compte_mots("je m'appelle ilyas omar houssein")








# exercice 3


# def inverse_chaine(chaine):
    
#     for i in range(3):
#         if i==0:
#             i=1
#             print(chaine[-i])
#         print(chaine[-i])
# inverse_chaine('ilyas')


#    un eleve a nom, adresse, genre , formation, matiere , note 




nomEleve=["Aicha Omar", "Ali farah", "fathia Abdo", "yahya Med" ]

AdresseEleve=["Balbala", "Q5", "Hodan", "Sheick Moussa"]

genre=["F", "M"]

formation=["programmation", "bureautique", "Maintenance", "design"]
i=0
# for nom in nomEleve:
# 	print('nom : '+ nom + " Adresse :" + AdresseEleve[i] + " genre : " + genre[i] )
# 	i+=1
noteAiche=[12, 16, 15]

noteAli=[17, 18, 19]

eleve={
	'nom': 'Aicha Omar',
	'Adresse':'Balbala',
	'genre':'F',
	'formation': 'programmation',
	'matiere': {'HTML5etcss3' : 12, 'gitetgithub': 16, 'figma' :15}

}


eleve2={
	'nom': 'Ali farah',
	'Adresse':'Q5',
	'gene':'M',
	'formation': 'bureautique',
	'matiere':{'word' : 17, 'excel': 18, 'powerpoint': 19}

}
eleve3={
	'nom': 'fathia Abdo',
	'Adresse':'hodan',
	'gene':'f',
	'formation': 'maintenance',
	'matiere':{'pc' : 10, 'fixe': 18, 'logiciel': 19}

}



def eleves(name, adress, gender, training , subjet={}):


	eleve={
		'nom': name,
		'Adresse':adress,
		'gene':gender,
		'formation': training,
		'matiere':subjet,
		'validé':'validé'
	}

	return eleve




nom="ilyas"

prenom= "Ali"


dictionnaie={
	'nom': nom,
	'prenom': prenom
}


# print(dictionnaie)

eleve1={}

eleve1=eleves('ilyas', 'pk12', 'M', 'design graphique', {'wireframme':12, 'maquette':16})
eleve2=eleves('fathia Abdo ', 'pk12', 'f', 'maintenance', {'pc' : 10, 'fixe': 18, 'logiciel': 19})
eleve3=eleves('youssouf Abdo ', 'Q1', 'M', 'maintenance', {'pc' : 19, 'fixe': 18, 'logiciel': 19})

print(eleve1)
print()
print(eleve2)
print()
print(eleve3)


# print( eleve['matiere']['HTML5etcss3']) 

# print(eleve2)