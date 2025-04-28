

fichier = open ("exemple.json", "r")
lignes = fichier.readlines()

#print(lignes)
candidat1 = "Nathaniel"
candidat2 = "Felix"
candidat3 = "Zakaria"

if lignes == "Nathaniel":
    candidat1 += 1
elif lignes == "Felix":
    candidat2 += 1
elif lignes == "Zakaria":
    candidat3 += 1


if candidat1 >= candidat2 and candidat3:
    print("Candidat 1 a gagné")
elif candidat2 >= candidat1 and candidat3:
    print("Candidat 2 a gagné")
elif candidat3 >= candidat1 and candidat2:
    print("Candidat 3 a gagné")
else:
    print("Il y a égalité")
fichier.close()
