from vpython import *
from intersections import *
class Scene:
    def __init__(self, title='', width=1280, height=720, background=color.white, center=vec(0, 0, 0), drag=True, gravity=True):
        background=color.white
        self.sc = canvas(title=title, width=width, height=height, background=background, center=center)
        self.boxes = []
        self.springs = []
        self.graphs = []
        self.drag = drag
        self.gravity = gravity
    def add_object(self, obj):
        self.boxes.append(obj)
    def add_spring(self, obj):
        self.springs.append(obj)
    def add_graph(self, graph):
        self.graphs.append(graph)
    def update(self, t, dt):
        totalforce = []
        totalforces = {}
        for box in self.boxes:
            totalforce.append(box.get_total_force())
            totalforces[box] = box.get_total_force()
            box.forces['friction'] = vec(0, 0, 0)
            box.forces['drag'] = drag(box) if self.drag else vec(0, 0, 0)
            box.forces['spring'] = vec(0, 0, 0)
            box.forces['gravity'] = vec(0, 0, 0)
            box.energies['kinetic'] = box.mass * mag2(box.velocity);
            box.energies['gravitational'] = 0;
        if self.gravity:
            for i in range(0, len(self.boxes)):
                for j in range(0, len(self.boxes)):
                    if i is not j:
                        self.boxes[i].forces['gravity'] += gravity(self.boxes[i], self.boxes[j]);
                        self.boxes[i].energies['gravitational'] += gravity_energy(self.boxes[i], self.boxes[j])
        
        for i in range(0, len(self.boxes)):
            for j in range(i+1, len(self.boxes)):
                if intersecting(self.boxes[i], self.boxes[j]):
                    m1 = self.boxes[i].mass
                    m2 = self.boxes[j].mass
                    u1 = self.boxes[i].velocity
                    u2 = self.boxes[j].velocity
                    x12 = self.boxes[i].get_pos() - self.boxes[j].get_pos();
                    x21 = -x12;
                    v1 = u1 - (2*m2)/(m1+m2) * dot(u1 - u2, x12)/mag2(x12) * x12;
                    v2 = u2 - (2*m1)/(m1+m2) * dot(u2 - u1, x21)/mag2(x21) * x21;
                    self.boxes[i].velocity = v1
                    self.boxes[j].velocity = v2
        for spring in self.springs:
            dirvec = norm(spring.obj1.get_pos() - spring.obj2.get_pos())
            dist = mag(spring.obj1.get_pos() - spring.obj2.get_pos()) - spring.length
            spring.obj1.forces['spring'] += -dist * spring.k * dirvec
            spring.obj2.forces['spring'] += dist * spring.k * dirvec
            spring.energy = spring.k * spring.get_stretched_length() / 2
        
        for box in self.boxes:
            box.update(dt)
        for spring in self.springs:
            spring.update()
        for graph in self.graphs:
            graph.update(t)
    def get_energy(self):
        energy = 0
        for box in self.boxes:
            energy += box.energies['kinetic'];
            energy += box.energies['gravitational'];
        for spring in self.springs:
            energy += spring.energy
        return energy
    def run(self, run_condition, change_forces, dt, superspeed=1):
        t = 0
        while run_condition():
            rate(1/dt)
            self.update(t, superspeed*dt)
            change_forces(t)
            t += dt
            print(self.get_energy())
        t -= dt
        return t

def drag(obj):
    if obj.type == 'sphere':
        return -norm(obj.velocity) * (1/2 * 1.225 * mag2(obj.velocity) * 0.47 * 3.14159 * obj.bx.radius**2)
    return vec(0, 0, 0)

grav_const = 6.67408e-11;

def gravity(on_object, from_object):
    return -norm(on_object.get_pos() - from_object.get_pos()) * grav_const * on_object.mass * from_object.mass / mag2(on_object.get_pos() - from_object.get_pos())
def gravity_energy(on_object, from_object):
    return - grav_const * on_object.mass * from_object.mass / mag(on_object.get_pos() - from_object.get_pos())