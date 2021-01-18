from vpython import *

class PhysicsGraph:
    def __init__(self, obj, xtitle, ytitle, desc, width=800, height=200, foreground=color.black, background=color.white, xmin=0, xmax=2.2, ymin=0, ymax=25):
        self.graph = graph(width=width, height=height, xtitle=xtitle, ytitle=ytitle, foreground=foreground, background=background, xmin=xmin, xmax=xmax, ymin=ymin, ymax=ymax)
        self.desc = desc
        self.obj = obj
        self.f = gcurve(graph=self.graph,color=color.red)
    def update(self, t):
        if self.desc == 'pos.x':
            self.f.plot(t, self.obj.bx.pos.x)
        if self.desc == 'pos.y':
            self.f.plot(t, self.obj.bx.pos.y)
        if self.desc == 'pos.z':
            self.f.plot(t, self.obj.bx.pos.z)
        if self.desc == 'velocity.x':
            self.f.plot(t, self.obj.velocity.x)
        if self.desc == 'velocity.y':
            self.f.plot(t, self.obj.velocity.y)
        if self.desc == 'velocity.z':
            self.f.plot(t, self.obj.velocity.z)
        if self.desc == 'speed':
            self.f.plot(t, self.speed())