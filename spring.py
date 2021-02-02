from vpython import *
class Spring:
    def __init__(self, k, obj1, obj2, length, radius=1):
        self.k = k
        self.obj1 = obj1
        self.obj2 = obj2
        self.length = length
        self.line = helix(pos=obj1.get_pos(), axis=obj2.get_pos()-obj1.get_pos(), radius=radius, coils=length/radius)
    def update(self):
        self.line.pos = self.obj1.get_pos()
        self.line.axis = self.obj2.get_pos()-self.obj1.get_pos()
    def get_stretched_length(self):
        return abs(length - mag(self.obj2.get_pos()-self.obj1.get_pos()))

