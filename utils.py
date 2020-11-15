

### Utilities ###

def isNum(n):
    try:
        float(str(n))
        return True
    except ValueError:
        return False
