from Point import strToPoint
from utils import extract_ents
import re

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
        self.__dict__.update(self.ppts)
        

### extra functions ###

#A function that takes a .ent file and return a list with the Entities()
def ent_file_to_objects(file):
    test_str = extract_ents(file)
    fullRange = r'\{.*?\}'
    regex = r"((\".*?\").?(\".*?\"))"
    ent_list = []
    ppt_list = []


    matchesFR = re.finditer(fullRange, test_str, re.MULTILINE | re.DOTALL)
    for matchNum, match in enumerate(matchesFR, start=1):
        ent_list.append("{match}".format(match = match.group().strip('{}')))

    for i in ent_list:
        matches = re.finditer(regex, i, re.DOTALL)
        e = Entity()
        for matchNum, match in enumerate(matches, start=1):
            e.addppts(**{f'{match.group(2)}'.strip('"'):f'{match.group(3)}'.strip('"')})
        ppt_list.append(e)

    return ppt_list


# A function to filter out certain entities from a list of Entities()
def filterEnts(entList):
    with open('ignorelist.config') as ignore:
        for line in ignore:
            entList[:] = [x for x in entList if not x.classname==line.strip('\n')]
            
    return entList

