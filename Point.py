import math

# Creates a 3-dimensional point (x,y,z)
class Point(object):

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    # Format the object string output to "x y z"
    def __str__(self):
        return f'{self.x} {self.y} {self.z}'

    # Moves a point by delta X,Y,Z
    def move(self, dx, dy, dz):
        self.x += dx
        self.y += dy
        self.z += dz

    # Returns the distance between two points
    def distance(self, other):
        return math.sqrt(math.pow(self.x - other.x, 2) + math.pow(self.y - other.y, 2) + math.pow(self.z - other.z, 2))

    