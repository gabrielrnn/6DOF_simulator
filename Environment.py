from Constants import *
import numpy as np

class Environment:
    def __init__(self):
        self.rho = Constants.RHO_0_kgpm3
        self.G = Constants.G_0_mps2 * np.array([0, 0, -1])
        

    def update(self):
        self.rho = Constants.RHO_0_kgpm3
        self.G = Constants.G_0_mps2 * np.array([0, 0, -1])
    
    def gravity(self):
        return self.G