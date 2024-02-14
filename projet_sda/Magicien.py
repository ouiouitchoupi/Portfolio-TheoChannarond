from Personnage import Personnage

class Magicien(Personnage):
    FORCE_FRAPPE_1 = 10
    FORCE_FRAPPE_2 = 15
    FORCE_FRAPPE_3 = 30
    FORCE_FRAPPE_4 = 0

    def __init__(self, nom, force):
        super().__init__(nom, force)

    def lance_un_sort(self, adversaire):
        force_frappe = self.get_force() + self.FORCE_FRAPPE_1
        self.frappe(adversaire, force_frappe)
        print(f"{self.get_nom()} lance un sort sur {adversaire.get_nom()} !")
        print(f"{adversaire.get_nom()} subit {force_frappe} points de dégâts.")
        print(f"Il reste {adversaire.get_vie()} points de vie à {adversaire.get_nom()}.")

    def lance_un_rayon_de_lumiere_sombre(self, adversaire):
        force_frappe = self.get_force() + self.FORCE_FRAPPE_2
        self.frappe(adversaire, force_frappe)
        print(f"{self.get_nom()} lance un rayon de lumière sombre sur {adversaire.get_nom()} !")
        print(f"{adversaire.get_nom()} subit {force_frappe} points de dégâts.")
        print(f"Il reste {adversaire.get_vie()} points de vie à {adversaire.get_nom()}.")
    
    def boule_de_feu_supreme(self, adversaire):
        force_frappe = self.get_force() + self.FORCE_FRAPPE_3
        self.frappe(adversaire, force_frappe)
        print(f"{self.get_nom()} lance une boule de feu suprême sur {adversaire.get_nom()} !")
        print(f"{adversaire.get_nom()} subit {force_frappe} points de dégâts.")
        print(f"Il reste {adversaire.get_vie()} points de vie à {adversaire.get_nom()}.")
    
    def magicien_a_peur(self, adversaire):
        force_frappe = self.get_force() + self.FORCE_FRAPPE_4
        self.frappe(adversaire, force_frappe)
        print(f"{self.get_nom()} a peur")

    def attaque(self, adversaire):
        random_attack = self.random_int(1, 4)
        if random_attack == 1:
            self.lance_un_sort(adversaire)
        elif random_attack ==2:
            self.lance_un_rayon_de_lumiere_sombre(adversaire)
        elif random_attack == 3:
            self.boule_de_feu_supreme(adversaire)
        else:
            self.magicien_a_peur(adversaire)
