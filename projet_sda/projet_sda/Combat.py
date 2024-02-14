from Magicien import Magicien
from RoiSorcier import RoiSorcier

class Combat:
    def demarrer_combat(self, magicien, roi_sorcier):
        while True:
            if magicien.tour == 'joueur1':
                magicien.attaque(roi_sorcier)
                magicien.tour = 'joueur2'
                roi_sorcier.tour = 'joueur1'
            else:
                roi_sorcier.attaque(magicien)
                magicien.tour = 'joueur1'
                roi_sorcier.tour = 'joueur2'

            if magicien.get_vie() <= 0:
                print(f"{magicien.get_nom()} n'est plus de ce monde !")
                print(f"{roi_sorcier.get_nom()} réussit finalement a en sortir vivant!")
                break
            elif roi_sorcier.get_vie() <= 0:
                print(f"{roi_sorcier.get_nom()}, a fini par perir,  sa mort était finalement inéluctable!")
                print(f"{magicien.get_nom()} remporte le duel !")
                break

if __name__ == "__main__":
    magicien = Magicien("Gandalf", 5)
    roi_sorcier = RoiSorcier("Sauron", 5)

    combat = Combat()
    combat.demarrer_combat(magicien, roi_sorcier)
