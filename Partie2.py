class Etudiant:
    def __init__(self, Name, prenom, age, cne, moyenne):
        self.Name = Name
        self.pre = prenom
        self.age = age
        self.cne = cne
        self.moyen = moyenne

    def __repr__(self):
        return '{ Nom: ' + self.Name + ', Prenom: ' + self.pre + ', Age: ' + str(self.age) + ', CNE: ' + str(self.cne) + ', Moyenne: ' + str(self.moyen) + '}\n'
    
# Remplissage de list de type Etudiant

etud = [
        Etudiant('Taha', 'RIDA', 21, 137524652, 20),
        Etudiant('Badr', 'Elmario', 22, 123789456, 20),
        Etudiant('hola', 'edriss', 18, 12784556, 15),
        Etudiant('Abas', 'fernass', 25 , 1289564523, 9)
    ]

# Affichage list ordonne par age
print("triez par age")
etud.sort(key=lambda x: x.age)
print(etud)

# Affichage list ordonne par moyenne
print("triez par moyenne")
etud.sort(key=lambda x: x.moyen)
print(etud)