import numpy as np

class Rocket:
    def __init__(self, mass = 50, inertia = None):
        self.mass_kg = mass
        self.inertia_kgpm2 = inertia
    
    def getMass_kg(self):
        return self.mass_kg
    