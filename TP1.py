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

 