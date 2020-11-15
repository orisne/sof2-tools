from utils import isNum


class Point:

    # Initializing a Point object (x,y,z) defaults to (0,0,0)
    def __init__(self, x=0 ,y=0 ,z=0):
        self.x = float(x) if isNum(x) else 0
        self.y = float(y) if isNum(y) else 0
        self.z = float(z) if isNum(z) else 0

    # Default string format
    def __str__(self):
        return f'{self.x} {self.y} {self.z}'

    # Moves a point
    def move(self, dx, dy, dz):
        self.x += float(dx) if isNum(dx) else 0
        self.y += float(dy) if isNum(dy) else 0
        self.z += float(dz) if isNum(dz) else 0

    # Overwrites the point coordinates with a new set
    def setCrds(self, nx, ny, nz):
        self.x = float(nx) if isNum(nx) else 0
        self.y = float(ny) if isNum(ny) else 0
        self.z = float(nz) if isNum(nz) else 0






### extra functions ###

# Takes a point in a string form ('0 0 0') and convert it into a Point object
def strToPoint(s=''):
    s = s.strip('\"').split(' ')
    try:
        p = Point(s[0], s[1], s[2])
    except IndexError:
        try:
            p = Point(s[0], s[1])
        except IndexError:
            try:
                p = Point(s[0])
            except:
                p = Point()
    return p