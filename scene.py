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
        if self.gravity:
            for i in range(0, len(self.boxes)):
                for j in range(0, len(self.boxes)):
                    if i is not j:
                        self.boxes[i].forces['gravity'] += gravity(self.boxes[i], self.boxes[j]);
        for spring in self.springs:
            dirvec = norm(spring.obj1.get_pos() - spring.obj2.get_pos())
            dist = mag(spring.obj1.get_pos() - spring.obj2.get_pos()) - spring.length
            spring.obj1.forces['spring'] += -dist * spring.k * dirvec
            spring.obj2.forces['spring'] += dist * spring.k * dirvec
        
        for box in self.boxes:
            box.update(dt)
        for spring in self.springs:
            spring.update()
        for graph in self.graphs:
            graph.update(t)
    def run(self, run_condition, change_forces, dt, superspeed=1):
        t = 0
        while run_condition():
            rate(1/dt)
            self.update(t, superspeed*dt)
            change_forces(t)
            t += dt
        t -= dt
        return t

def drag(obj):
    if obj.type == 'sphere':
        return -norm(obj.velocity) * (1/2 * 1.225 * mag2(obj.velocity) * 0.47 * 3.14159 * obj.bx.radius**2)
    return vec(0, 0, 0)

grav_const = 6.67408e-11;

def gravity(on_object, from_object):
    return -norm(on_object.get_pos() - from_object.get_pos()) * grav_const * on_object.mass * from_object.mass / mag2(on_object.get_pos() - from_object.get_pos())