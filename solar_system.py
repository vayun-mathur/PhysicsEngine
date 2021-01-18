#models a small satellite orbiting a planet

from vpython import *
from lib import *

def round_digits(number, digits):
    return round(number * 10**digits)/10**digits

sc = Scene('Solar System', center=vec(0,0,0), drag=False, gravity=True)

earth = PhysicsBox(type='sphere', pos=vec(0,0,0), velocity=vec(0, 0, 0), radius = 6_371_000, color=color.red, mass=5.972e24, make_trail=True)
satellite = PhysicsBox(type='sphere', pos=vec(0,7_371_000,0), velocity=vec(7_350, 0, 0), radius = 60_000, color=color.red, mass=1000)
sc.add_object(satellite)
sc.add_object(earth)

def run_condition():
    return True

def change_forces(t):
    pass

t = sc.run(run_condition, change_forces, 0.001, superspeed=1000)
