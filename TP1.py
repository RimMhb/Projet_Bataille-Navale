from math import sqrt


class NoAmmunitionError(Exception):
    pass
class OutOfRangeError(Exception):
    pass

class Weapon:
    def __init__(self,ammunitions,range) -> None:
        self.ammunations = ammunitions
        self.range = range
    def fire_at(self,x,y,z):
        if self.ammunations == 0:
            raise NoAmmunitionError
        self.ammunations -= 1
        if sqrt(x**2 + y**2) > self.range:
            raise OutOfRangeError
            
            
"""Les 3 armes:"""

"""Lance missile anti-surface"""
class Arme_LMS(Weapon):
    def __init__(self) -> None:
        super().__init__(40, 30)
    def fire_at(self,x, y, z):
        super().fire_at(x,y,z)
        if z != 0:
            raise OutOfRangeError

"""Lance missile anti-air"""
class Arme_LMA(Weapon):
    def __init__(self) -> None:
        super().__init__(50, 40)
    def fire_at(self,x, y,z):
        super().fire_at(x,y,z)
        if z <= 0:
            raise OutOfRangeError

"""Lance torpilles"""
class Arme_LT(Weapon):
    def __init__(self) -> None:
        super().__init__(15, 20)
    def fire_at(self,x, y,z):
        super().fire_at(x,y,z)
        if z > 0:
            raise OutOfRangeError


 
