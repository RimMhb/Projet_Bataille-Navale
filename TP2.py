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
        class Cruiser(Vessel):
    def __init__(self, coordinates: Tuple, max_hits: int, weapon: Weapon):
        super().__init__(coordinates, 6, Arme_LMA())
    def go_to(self, x, y, z):
        if z==0:
            super().go_to(x,y,z)

class Submarine(Vessel):
    def __init__(self, coordinates: Tuple, max_hits: int, weapon: Weapon):
        super().__init__(coordinates, 2, Arme_LT())
    def go_to(self, x, y, z):
        if z<0:
            super().go_to(x, y, z)
    
class Fregate(Vessel):
    def __init__(self, coordinates: Tuple, max_hits: int, weapon: Weapon):
        super().__init__(coordinates, 5, Arme_LMS())
    def go_to(self, x, y, z):
        if z == 0:
            super().go_to(x, y, z)

class Destroyer(Vessel):
    def __init__(self, coordinates: Tuple, max_hits: int, weapon: Weapon):
        super().__init__(coordinates, 4, Arme_LT())
    def go_to(self, x, y, z):
        if z == 0:    
            super().go_to(x, y, z)
    
class Aircraft(Vessel):
    def __init__(self, coordinates: Tuple, max_hits: int, weapon: Weapon):
        super().__init__(coordinates, 1, Arme_LMS())
    def go_to(self, x, y, z):
        if z == 1:
            super().go_to(x, y, z)    

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
