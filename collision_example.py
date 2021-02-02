#models collision of two spheres

from vpython import *
from lib import *

def round_digits(number, digits):
    return round(number * 10**digits)/10**digits

sc = Scene('Collision', center=vec(0,0,0), drag=False, gravity=False)

ball1 = PhysicsBox(type='sphere', pos=vec(0.5,0,0), velocity=vec(0, 2, 0), radius = 2, color=color.red, mass=8)
ball2 = PhysicsBox(type='sphere', pos=vec(0,10,0), velocity=vec(0, -1, 0), radius = 1, color=color.red, mass=1)
sc.add_object(ball1)
sc.add_object(ball2)

def run_condition():
    return True

def change_forces(t):
    pass

t = sc.run(run_condition, change_forces, 0.001)

