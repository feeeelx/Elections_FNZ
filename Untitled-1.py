fichier = open ("Dossier_externe.json", "r")
fichier.write("Liste électoral :\n")
fichier.write("Nathaniel\n")
fichier.write("Felix\n")
fichier.write("Zakaria\n")
fichier.close()

fichier = open ("Dossier_externe.json", "r")
lignes = fichier.readlines()
print(lignes)
candidat1 = "Nathaniel"
candidat2 = "Felix"
candidat3 = "Zakaria"

if lignes[1] == "Nathaniel":
    candidat1 += 1
if lignes[2] == "Felix":
    candidat2 += 1
if lignes[3] == "Zakaria":
    candidat3 += 1
if candidat1 > candidat2 and candidat3:
    print("Candidat 1 a gagné")
elif candidat2 > candidat1 and candidat3:
    print("Candidat 2 a gagné")
elif candidat3 > candidat1 and candidat2:
    print("Candidat 3 a gagné")
else:
    print("Il y a égalité")
fichier.close()
