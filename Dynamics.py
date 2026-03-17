import numpy as np
import Environment

class Dynamics:
    """ 6 DOF dynamics from an inertial system of coordinates: X = [x y z xDot yDot zDot theta phi psi thetaDot phiDot psiDot]
        Uses Euler's method"""
    def __init__(self, mass = None, dt = None, r0 = np.zeros(3), v0 = np.zeros(3), phi0 = np.zeros(3), phiDot0 = np.zeros(3)):
        assert mass != None, "Mass must be defined"
        assert dt != None, "Time step must be defined"
        self.r_cm = r0
        self.v_cm = v0
        self.phi = phi0
        self.phiDot = phiDot0
        self.translational = np.append(self.r_cm, self.v_cm)
        self.angular = np.append(self.phi, self.phiDot)
        self.X = np.append(self.translational, self.angular)
        self.m = float(mass)
        self.dt = float(dt)
        
    
    def update(self, F = np.zeros(3)):
        # TODO: Implement Aerodynamic and Propulsive forces
        env = Environment.Environment()
        g = env.gravity()
        self.r_cm += self.v_cm * self.dt
        self.v_cm += (F / self.m + g) * self.dt
        self.phi += np.zeros(3)
        self.phiDot += np.zeros(3) # TODO: Implement angular dynamics
        self.translational = np.append(self.r_cm, self.v_cm)
        self.angular = np.append(self.phi, self.phiDot)
        self.X = np.append(self.translational, self.angular)
    
    def getPosition(self):
        return self.r_cm
    
    def getVelocities(self):
        return self.v_cm
    
    def getEulerAngles(self):
        return self.phi
    
    def getEulerAngleRates(self):
        return self.phiDot
    
    def getStateVector(self):
        return self.X


def runSanityChecksDynamics():
    print("Running Sanity Checks for Dynamics.py")
    try:
        Dynamics(mass = 1, dt = 0.01)
    except AssertionError:
        print("\t *Implementation checks if mass and time step are defined")
