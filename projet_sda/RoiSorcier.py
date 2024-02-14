from Personnage import Personnage

class RoiSorcier(Personnage):
    FORCE_FRAPPE_1 = 5
    FORCE_FRAPPE_2 = 20
    FORCE_FRAPPE_3 = 35
    FORCE_FRAPPE_4 = 0

    def __init__(self, nom, force):
        super().__init__(nom, force)

    def frappe_avec_son_epee(self, adversaire):
        force_frappe = self.get_force() + self.FORCE_FRAPPE_1
        self.frappe(adversaire, force_frappe)
        print(f"{self.get_nom()} attaque avec son épée sur {adversaire.get_nom()} !")
        print(f"{adversaire.get_nom()} subit {force_frappe} points de dégâts.")
        print(f"Il reste {adversaire.get_vie()} points de vie à {adversaire.get_nom()}.")

    def attaque_avec_son_nazgul(self, adversaire):
        force_frappe = self.get_force() + self.FORCE_FRAPPE_2
        self.frappe(adversaire, force_frappe)
        print(f"{self.get_nom()} attaque avec son nazgul sur {adversaire.get_nom()} !")
        print(f"{adversaire.get_nom()} subit {force_frappe} points de dégâts.")
        print(f"Il reste {adversaire.get_vie()} points de vie à {adversaire.get_nom()}.")
    
    def empoissement(self, adversaire):
        force_frappe = self.get_force() + self.FORCE_FRAPPE_3
        self.frappe(adversaire, force_frappe)
        print(f"{self.get_nom()} empoissone {adversaire.get_nom()} !")
        print(f"{adversaire.get_nom()} subit {force_frappe} points de dégâts.")
        print(f"Il reste {adversaire.get_vie()} points de vie à {adversaire.get_nom()}.")
    
    def RoiSorcie_a_peur(self, adversaire):
        force_frappe = self.get_force() + self.FORCE_FRAPPE_4
        self.frappe(adversaire, force_frappe)
        print(f"{self.get_nom()} a peurs")

    def attaque(self, adversaire):
        random_attack = self.random_int(1, 4)
        if random_attack == 1:
            self.frappe_avec_son_epee(adversaire)
        elif random_attack == 2:
            self.attaque_avec_son_nazgul(adversaire)
        elif random_attack == 3:
            self.empoissement(adversaire)
        else:
            self.RoiSorcie_a_peur(adversaire)