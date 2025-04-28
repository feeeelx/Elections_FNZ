

fichier = open ("exemple.json", "r")
lignes = fichier.readlines()

#print(lignes)
candidat1 = "Nathaniel"
candidat2 = "Felix"
candidat3 = "Zakaria"


votes_candidat1 = 0
votes_candidat2 = 0
votes_candidat3 = 0

for ligne in lignes:
    ligne = ligne.strip()  
    if ligne == "Nathaniel":
        votes_candidat1 += 1
    elif ligne == "Felix":
        votes_candidat2 += 1
    elif ligne == "Zakaria":
        votes_candidat3 += 1

if votes_candidat1 >= votes_candidat2 and votes_candidat1 >= votes_candidat3:
    print("Candidat 1 a gagné")
elif votes_candidat2 >= votes_candidat1 and votes_candidat2 >= votes_candidat3:
    print("Candidat 2 a gagné")
elif votes_candidat3 >= votes_candidat1 and votes_candidat3 >= votes_candidat2:
    print("Candidat 3 a gagné")
else:
    print("Il y a égalité")


fichier.close()
