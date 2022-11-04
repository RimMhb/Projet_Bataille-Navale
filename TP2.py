from typing import Tuple

from TP1 import Weapon
from TP1 import Arme_LMS, Arme_LMA, Arme_LT

class DestroyedError(Exception):
    pass

class Vessel:
    def __init__(self,coordinates : Tuple, max_hits: int, weapon : Weapon ):
        self.coordinates = coordinates
        self.max_hits = max_hits
        self.weapon = weapon

    def go_to(self,x,y,z):
        self.coordinates = (x,y,z)
    def get_coordinates(self):
        return self.coordinates
    def fire_at(self,x,y,z):
        if self.max_hits == 0:
            raise DestroyedError
        self.weapon.fire_at(x,y,z)
