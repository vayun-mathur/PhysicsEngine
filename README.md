# Physics Engine
## What is this?

This is a physics engine that utilizes the VPython library for rendering.
### Features
* Boxes and Spheres (the actual physically interacting objects)
* Springs
* Air resistance (for spheres only)
* Gravity
* Graphs
## Getting Started
### Installation
1. Start by cloning the repository with `git clone https://github.com/vayunmathur/PhysicsEngine`
2. Open "PhysicsEngine.sln" in Visual Studio
3. Everything should work!
### Documentation
#### Creating a Scene
Before running any physics you must create a scene object:
`Scene(title='', width=1280, height=720, background=color.white, center=vec(0,0,0), drag=False, gravity=False)`
1. title: title of the simulation
2. width: width of the viewport in pixels
3. height: height of the viewport in pixels
4. background: color of the background
5. center: where the camera starts off pointing to
6. drag: enable or disable air resistance
7. gravity: enable or disable gravitational accelerations
#### Creating a physics object
To create a physics object you have to use the `PhysicsBox` constructor:
`PhysicsBox(type='box', mass=1, pos=vec(0, 0, 0), axis=vec(1, 0, 0), size=vec(1, 1, 1), color=color.black, radius=1, make_trail=False, trail_type="points", interval=10, velocity=vec(0, 0, 0), texture=textures.metal)`
The parameters mean as follows:
1. type: "box" or "sphere" specifies the shape of the physics object
2. mass: mass for simulating physics
3. pos: initial position of the center of the object
4. axis: initial rotation of the object
5. size: dimensions of the object (only applies to box)
6. color: color of object (no impact on physics)
7. radius: radius of the object (only applies to sphere)
8. make_trail: enables creation of trail behind object
9. trail_type: visual appearance of the trail
10. interval: gap between points in trail
11. velocity: initial velocity of the object
12. texture: visual texture of the object (no impact of physics, yet)

To add the object to the scene, you use `scene.add_object(object)`

#### Creating a spring
`Spring(k, obj1, obj2, length, radius=1)`
Parameters:
1. k: spring constant of the spring
2. obj1: physics object attached to one end of the spring
3. obj2: physics object attached to other end of the spring
4. length: default length of spring when no force is exerted
5. radius: radius of the helix

To add the spring to the scene, you use `scene.add_spring(spring)`

#### Run your scene
`t = scene.run(run_condition, change_forces, dt, superspeed=1)`
Parameters:
1. run_condition: a function that returns `False` when the simulation should terminate
2. change_forces: a function that is called once per update that is generally used to update the forces on an object through the execution of the program. WARNING: This is now deprecated and you should not use this
3. dt: the change in time between frames
4. superspeed: factor between simulation time and real time

Returns the execution time of the program in real time.