from Point import Point

# Creates an entity
class Entity:
    
    # Initializes an entity with a classname and an empty list of attributes
    #* attributes has to be a single list of smaller 2 length lists for example:
    #* [ ['key', 'value'], ['key', 'value'], ['key', 'value'] ]
    def __init__(self, classname='temp', attributes=[]):
        self.classname = classname
        self.attributes = attributes

    # Formatting the entity syntax to fit into the .ent file
    def __str__(self):
        t = '{' + f'\n"classname" "{self.classname}"\n'
        for i in self.attributes:
            t += f'"{i[0]}" "{i[1]}"\n'
        t += '}'
        return t

    # Moves an entitiy's origin by delta x,y,z (only if it has an origin property)
    def move(self, dx, dy, dz):
        for i, ppt in enumerate(self.attributes):
            if 'origin' in ppt:
                x = ppt[1].split(' ')
                p = Point(int(x[0]), int(x[1]), int(x[2]))
                p.move(int(dx), int(dy), int(dz))
                self.attributes[i][1] = str(p)
                break
                
    # Adds one or more attributes to the list, 
    #* same syntax as __init__
    def add_attributes(self, ppts):
        for i in ppts:
            self.attributes.append(i)

    # Changes an existing property value, 
    #* key='property_name' and value='value'
    def change_value(self, key, value):
        # checks if a the key to change is the classname, if so changes the self.classname
        if key == 'classname':
            self.classname = value
        else:
            for i, ppt in enumerate(self.attributes):
                if key in ppt:
                    self.attributes[i][1] = value
                    break

    # Checks if two entities share the same classname value, returns True if they do.
    def compare_classnames(self, other):
        if self.classname == other.classname:
            return True
        else:
            return False
