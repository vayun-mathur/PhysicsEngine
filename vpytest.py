from vpython import *
from lib import *

def round_digits(number, digits):
    return round(number * 10**digits)/10**digits

scene = Scene('1D Accelerated Motion Assignment #3', center=vec(10,5,-10), drag=False, gravity=False)

ground1 = PhysicsBox(pos=vec(-5,5,0), size = vec(5,.5,2), color=color.green, mass=10000)
ground2 = PhysicsBox(pos=vec(10,5,0), size = vec(5,.5,2), color=color.green, mass=10000)
marble = PhysicsBox(type='sphere', pos=vec(0,-10,0), radius = 0.5, color=color.blue)
center = PhysicsBox(type='sphere', pos=vec(0,-5,0), radius = 0.5, color=color.red)
spring1 = Spring(3, ground1, center, 7, radius=0.1)
spring2 = Spring(3, ground2, center, 11, radius=0.1)
spring3 = Spring(3, center, marble, 5, radius=0.1)
scene.add_object(marble)
scene.add_object(center)
scene.add_object(ground1)
scene.add_object(ground2)
scene.add_spring(spring1)
scene.add_spring(spring2)
scene.add_spring(spring3)

def run_condition():
    return True

def change_forces(t):
    pass

marble.set_force("gravity", vec(0, -9.8, 0))

t = scene.run(run_condition, change_forces, 0.001)