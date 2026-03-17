import numpy as np
import matplotlib.pyplot as plt
import Rocket, Dynamics, Environment

class Simulation:
    def __init__(self, t0 = 0, tf = 10, dt = 0.01, X0 = np.zeros(12)):
        """Initializes initial time with t0, step length with dt and stop time with tf.
        Also creates a time vector t with these parameters."""
        assert tf > t0, "Stop time must be bigger than initial time"
        assert dt > 0, "Step time must be positive"
        self.t0, self.tf, self.dt = t0, tf, dt
        self.t = np.arange(t0, tf, dt)
        self.t_index = 0
        self.X_t = np.zeros([12,len(self.t)])
        self.X_t[:, 0] = X0

    
    def step(self):
        assert self.t_index >= 0, "Index must be bigger than -1"
        self.t_index += 1
    
    def getStateHistory(self):
        return self.t, self.X_t
    
    def run(self):
        vehicle = Rocket.Rocket()
        self.env = Environment.Environment()
        m = vehicle.getMass_kg()
        self.dynamics = Dynamics.Dynamics(mass = m, dt = self.dt)
        for i, _ in enumerate(self.t):
            self.env.update()
            self.dynamics.update()
            self.X_t[:, i] = self.dynamics.getStateVector()
            self.step()

def runSanityChecksSimulation():
    print("Running Sanity Checks for Simulation.py:")
    try:
        Simulation(0, -1, 0.01)
    except AssertionError:
        print("\t *Implementation checks if tf > t0")

    try:
        Simulation(0, -1, -0.01)
    except AssertionError:
        print("\t *Implementation checks if step time is positive") 

runSanityChecksSimulation()

simul = Simulation()
simul.run()


t, X = simul.getStateHistory()

fig, ax = plt.subplots()

ax.plot(t, X[2,:])
plt.show()