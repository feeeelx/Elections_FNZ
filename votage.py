# dict_infos = {}

nom = input("Votre nom complet, sans middle name: ")
rue = input("Entrez le nom de votre rue: ")
age = input("Votre age: ")


dict_infos = {
    "nom": nom,
    "rue": rue,
    "age": age
}
for i in dict_infos.keys():
    print(dict_infos[i])