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

        class Battlefield:
    def __init__(self):
        self.vessels = []

    def add_vessel(self,vessel):
        coor = vessel.get_coordinates()
        max_hits = vessel.max_hits
        for existing_vessel in self.vessels:
            if existing_vessel.get_coordinates() == coor:
                return False
            max_hits += existing_vessel.max_hits
        if max_hits > 22:
            return False
        self.vessels.append(vessel)
    
    def receive(self,x,y,z):
        coor = (x,y,z)
        for existing_vessel in self.vessels:
            if existing_vessel.get_coordinates() == coor:
                return True
        return False
