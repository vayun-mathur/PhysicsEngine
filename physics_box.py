from vpython import *
class PhysicsBox:
    def __init__(self, type='box', mass=1, pos=vec(0, 0, 0), axis=vec(1, 0, 0), size=vec(1, 1, 1), color=color.black, radius=1, make_trail=False, trail_type="points", interval=10, velocity=vec(0, 0, 0), texture=textures.metal, isSolid=False):
        self.type = type
        if type == 'box':
            self.bx = box(pos=pos, axis=axis, size=size, color=color, make_trail=make_trail, trail_type=trail_type, interval=interval, texture=texture)
        if type == 'sphere':
            self.bx = sphere(pos=pos, axis=axis, size=size, color=color, make_trail=make_trail, trail_type=trail_type, interval=interval, radius=radius, texture=texture)
        self.velocity = velocity
        self.isSolid = isSolid
        self.prev_velocity = velocity
        self.forces = {}
        self.mass = mass
    def get_pos(self):
        return self.bx.pos
    def set_force(self, force_name, force_vector):
        self.forces[force_name] = force_vector
    def remove_force(self, force_name):
        self.forces.pop(force_name)
    def speed(self):
        return mag(self.velocity)
    def get_total_force(self):
        force = vec(0, 0, 0)
        for name in self.forces:
            force += self.forces[name]
        return force / self.mass
    def update(self, dt):
        self.bx.pos += self.velocity * dt
        self.prev_velocity = self.velocity
        self.velocity += self.get_total_force() * dt
