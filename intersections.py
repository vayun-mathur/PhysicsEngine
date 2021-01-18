from vpython import *

def intersect_sphere_box(sphere, box):
    closest = vec(max(box.bx.pos.x-box.bx.size.x/2, min(sphere.bx.pos.x, box.bx.pos.x+box.bx.size.x/2)), max(box.bx.pos.y-box.bx.size.y/2, min(sphere.bx.pos.y, box.bx.pos.y+box.bx.size.y/2)), max(box.bx.pos.z-box.bx.size.z/2, min(sphere.bx.pos.z, box.bx.pos.z+box.bx.size.z/2)))
    return mag(closest - sphere.bx.pos) <= sphere.bx.radius

def intersection_sphere_box(sphere, box):
    return vec(max(box.bx.pos.x-box.bx.size.x/2, min(sphere.bx.pos.x, box.bx.pos.x+box.bx.size.x/2)), max(box.bx.pos.y-box.bx.size.y/2, min(sphere.bx.pos.y, box.bx.pos.y+box.bx.size.y/2)), max(box.bx.pos.z-box.bx.size.z/2, min(sphere.bx.pos.z, box.bx.pos.z+box.bx.size.z/2)))

def intersection_sphere_sphere(sphere1, sphere2):
    d = mag(sphere2.bx.pos - sphere1.bx.pos)
    x = (d**2 - sphere2.bx.radius**2 + sphere1.bx.radius**2) / (2 * d)
    return x * norm(sphere2.bx.pos - sphere1.bx.pos)


def intersection(obj1, obj2):
    if obj1.type == 'sphere' and obj2.type == 'sphere':
        return intersection_sphere_sphere(obj1,  obj2)
    if obj1.type == 'sphere' and obj2.type == 'box':
        return intersection_sphere_box(obj1, obj2)
    if obj1.type == 'box' and obj2.type == 'sphere':
        return intersection_sphere_box(obj2, obj1)

def intersecting(obj1, obj2):
    if obj1.type == 'sphere' and obj2.type == 'sphere':
        return mag(obj1.bx.pos - obj2.bx.pos) <= obj1.bx.radius + obj2.bx.radius
    if obj1.type == 'sphere' and obj2.type == 'box':
        return intersect_sphere_box(obj1, obj2)
    if obj1.type == 'box' and obj2.type == 'sphere':
        return intersect_sphere_box(obj2, obj1)