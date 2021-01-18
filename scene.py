from vpython import *
from intersections import *
class Scene:
    def __init__(self, title='', width=1280, height=720, background=color.white, center=vec(0, 0, 0), drag=True):
        background=color.white
        self.sc = canvas(title=title, width=width, height=height, background=background, center=center)
        self.boxes = []
        self.springs = []
        self.graphs = []
        self.drag = drag
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
            box.forces['normal'] = vec(0, 0, 0)
            box.forces['friction'] = vec(0, 0, 0)
            box.forces['drag'] = drag(box) if self.drag else vec(0, 0, 0)
            box.forces['spring'] = vec(0, 0, 0)
        for spring in self.springs:
            dirvec = norm(spring.obj1.get_pos() - spring.obj2.get_pos())
            dist = mag(spring.obj1.get_pos() - spring.obj2.get_pos()) - spring.length
            spring.obj1.forces['spring'] += -dist * spring.k * dirvec
            spring.obj2.forces['spring'] += dist * spring.k * dirvec
        for i in range(0, len(self.boxes)):
            box1 = self.boxes[i]
            for j in range(0, len(self.boxes)):
                box2 = self.boxes[j]
                if box1 is not box2 and intersecting(box1, box2):
                    inter = box1.bx.pos+vec(0, -1, 0)#intersection(box2, box1)
                    dirvec = norm(inter - box1.bx.pos)
                    normalforce = mag(totalforce[i]) * dirvec * -dot(norm(totalforce[i]), dirvec)
                    box1.forces['normal'] += normalforce
                    box1.forces['friction'] += 0.5 * mag(normalforce) * -norm(box1.velocity)
                    #box1.velocity = box1.velocity - 2 * dot(box1.velocity, dirvec) * dirvec
        
        for box in self.boxes:
            box.update(dt)
        for spring in self.springs:
            spring.update()
        for graph in self.graphs:
            graph.update(t)
    def run(self, run_condition, change_forces, dt):
        t = 0
        while run_condition():
            rate(1/dt)
            self.update(t, dt)
            change_forces(t)
            t += dt
        t -= dt
        return t

def drag(obj):
    if obj.type == 'sphere':
        return -norm(obj.velocity) * (1/2 * 1.225 * mag2(obj.velocity) * 0.47 * 3.14159 * obj.bx.radius**2)
    return vec(0, 0, 0)