from Point import strToPoint

class Entity:

    # Initializing a new Entity with keyword arguments
    def __init__(self, **ppts):
        self.ppts = ppts

        # Checks if one of the keys is an origin and if so make it a Point object
        for k, v in self.ppts.items():
            if k == 'origin':
                if type(v) == str:
                    self.ppts[k] = strToPoint(v)

        # Updates the dictionary of the class (to use as Entity.keyword)
        self.__dict__.update(ppts)


    # Sets the default string format for the class (ready for the .ent file)
    def __str__(self):
        s = '{\n'
        for key, value in self.ppts.items():
            s += f'\"{key}\" \"{value}\"\n'
        return s + '}'


    # Moves only the origin of an Entity object
    def moveOrigin(self, dx=0, dy=0, dz=0):
        for key, value in self.ppts.items():
            if key == 'origin':
                value.move(dx,dy,dz)
                self.ppts[key] = value

    # Changes an existing value of a key (ex: Entity.changeValue('classname', 'NEW_classname'))
    def changeValue(self, k, v):
        self.ppts[k] = v

    # Adding new properties to exsiting Entity (usefull for target/targetnames for example)
    def addppts(self, **newprops):
        for k, v in newprops.items():
            if k=='origin':
                newprops[k] = strToPoint(v)
        self.ppts.update(newprops)






### extra functions ###

# Loads a ent file and returns a list of all the Entities inside as Entity objects
def loadEntFile(file):
    entList = []

    with open(file) as f:

        _ents = f.read().replace('{\n', '').split('\n}\n')
        _ents.remove(_ents[-1])

        for _ent in _ents:
            e = Entity()
            _ppts = _ent.split('\n')

            for line in _ppts:
                e.addppts(**{line.split('\" \"')[0].replace('\"', ''): line.split('\" \"')[1].replace('\"', '')})

            entList.append(e)
    return entList