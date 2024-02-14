import random

class Personnage:
    def __init__(self, nom, force):
        self._nom = nom
        self._vie = 100
        self._force = force
        self._experience = 0
        self._degats = 0
        self.tour = 'joueur1'

    def get_nom(self):
        return self._nom

    def set_nom(self, nom):
        self._nom = nom

    def get_vie(self):
        return self._vie

    def set_vie(self, vie):
        self._vie = vie

    def get_force(self):
        return self._force

    def set_force(self, force):
        self._force = force

    def get_experience(self):
        return self._experience

    def set_experience(self, experience):
        self._experience = experience

    def get_degats(self):
        return self._degats

    def set_degats(self, degats):
        self._degats = degats

    def frappe(self, cible, force_frappe):
        if self.tour == 'joueur1':
            self.tour = 'joueur2'
        else:
            self.tour = 'joueur1'

        cible.recoit_degat(self, force_frappe)
        self._experience += 1
        self._force += self._experience

    def esquive(self):
        pass

    def recoit_degat(self, adversaire, force_frappe):
        self._degats += force_frappe
        self._vie -= force_frappe
        if self._vie == 0:
            print(f"{self._nom} est desormais plus de ce monde ")
            exit()

    def random_int(self, a, b):
        return random.randint(a, b)
