import re

### Utilities ###

# Checks if a value is a valid number (int/float)
def isNum(n):
    try:
        float(str(n))
        return True
    except ValueError:
        return False


def extract_ents(file):
    with open(file, 'r', errors='ignore') as f:
        regex = r'\{(\n\".*)*\"\n\}'
        test_str = f.read()
        matches = re.finditer(regex, test_str, re.VERBOSE)
        content = ''

        for match in matches:
            content += ((match.group(0))+ '\n')

        return content

