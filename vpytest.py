from vpython import *
from graph import PhysicsGraph
from scene import Scene
from intersections import intersecting
from spring import Spring
from physics_box import PhysicsBox

def round_digits(number, digits):
    return round(number * 10**digits)/10**digits

#create scene
scene = Scene('1D Accelerated Motion Assignment #3', center=vec(10,5,-10), drag=False)

'''
#create ball and add to scene
ground = PhysicsBox(pos=vec(0,-10.5,0), size = vec(20,.5,2), color=color.green, isSolid=True, mass=10000)
table = PhysicsBox(pos=vec(-5,-1,0), size = vec(10,1,2), texture=textures.wood, isSolid=True)
leg1 = PhysicsBox(pos=vec(-9,-5.5,0), size = vec(.5,10,.5), texture=textures.wood, isSolid=True)
leg2 = PhysicsBox(pos=vec(-1,-5.5,0), size = vec(.5,10,.5), texture=textures.wood, isSolid=True)
marble = PhysicsBox(type='sphere', pos=vec(-9,0,0), radius = 0.5, color=color.blue, make_trail=True, trail_type="points", interval=200, velocity=vec(1, 0, 0))
marble2 = PhysicsBox(type='sphere', pos=vec(-5,0,0), radius = 0.5, color=color.green, make_trail=True, trail_type="points", interval=200, velocity=vec(-1, 0, 0))
scene.add_object(marble)
scene.add_object(marble2)
scene.add_object(table)
#scene.add_object(leg1)
#scene.add_object(leg2)
scene.add_object(ground)
'''
ground1 = PhysicsBox(pos=vec(-5,5,0), size = vec(5,.5,2), color=color.green, isSolid=True, mass=10000)
ground2 = PhysicsBox(pos=vec(10,5,0), size = vec(5,.5,2), color=color.green, isSolid=True, mass=10000)
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
#marble2.set_force("gravity", vec(0, -9.8, 0))
t = scene.run(run_condition, change_forces, 0.001)