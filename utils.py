import re

from Point import Point
from Entity import Entity

# Extracts and formats the entity code from a text 
#* returns a collection of entities in string format
def format_entities(string):
    regex = r'\{(\n\".*)*\"\n\}'
    test_str = string
    matches = re.finditer(regex, test_str, re.VERBOSE)
    content = ''

    for match in matches:
        content += ((match.group(0))+ '\n')

    return content

# Takes entities in string form and returns a list of Entity objects
#* returns a list of entities (python objects)
def str_to_entities(string):
    test_str = format_entities(string)
    fullRange = r'\{.*?\}'
    regex = r"((\".*?\").?(\".*?\"))"
    list_of_text_entities = []
    entities_list = []
    
    matchesFR = re.finditer(fullRange, test_str, re.MULTILINE | re.DOTALL)
    for match in matchesFR:
        list_of_text_entities.append("{match}".format(match = match.group()))

    for i in list_of_text_entities:
        matches = re.finditer(regex, i, re.DOTALL)
        attr = []
        for match in matches:
            if 'classname' in match.group():
                class_name = match.group(3).strip('"')
                continue
            attr.append([match.group(2).strip('"'), match.group(3).strip('"')])
        entities_list.append(Entity(class_name, attr))

    return entities_list

# Filters unwanted Entities from a list of Entity objects, determined by classnames
#* returns a list of entities after filtration
def filter_entities(ent_list):
    try:
        with open('ignore.list') as ignore:
            for i in ignore:
                ent_list[:] = [x for x in ent_list if not x.classname==i.strip('\n')]

        return ent_list
    except:
        print('missing ignore.list file!')

# Fills a 3D rectangular box using two points objects as corners
#* reuturns a list of point objects
def fill(point_1=Point(), point_2=Point(10,10,10), offset=Point(10,10,10), hollow=False):
    
    points = []
    offset = Point(abs(offset.x), abs(offset.y), abs(offset.z))
    p1 = Point(min(point_1.x, point_2.x), min(point_1.y, point_2.y), min(point_1.z, point_2.z))
    p2 = Point(max(point_1.x, point_2.x), max(point_1.y, point_2.y), max(point_1.z, point_2.z))
    
    # if user set offset to 0 sets it to the distance + 1 (to run atleast once in for loop)
    offset.x = p2.x-p1.x+1 if offset.x == 0 else offset.x
    offset.y = p2.y-p1.y+1 if offset.y == 0 else offset.y
    offset.z = p2.z-p1.z+1 if offset.z == 0 else offset.z
    
    # setting the border of the rectangle for Hollowing
    border = [p1.x, 
              p1.y, 
              p1.z, 
              int((p2.x-p1.x)), 
              int((p2.y-p1.y)), 
              int((p2.z-p1.z))]
    
    # Loops through the axii and fill in the points in offset intervals
    for i in range(p1.z, p2.z+1, offset.z):
        for j in range(p1.y, p2.y+1, offset.y):
            for k in range(p1.x, p2.x+1, offset.x):
                if hollow:
                    if any([i in border,j in border,k in border]):
                        points.append((Point(k,j,i)))
                    else:
                        continue
                else:
                    points.append(Point(k,j,i))

    return points


