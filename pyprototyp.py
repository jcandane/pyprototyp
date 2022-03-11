import numpy as np 
import inspect, sys
import IPython
from IPython.core.magics.code import extract_symbols

π = np.pi 

def new_getfile(object, _old_getfile=inspect.getfile):
    ### Evann Courdier Jan 20, 2021 at 9:01: https://stackoverflow.com/questions/51566497
    if not inspect.isclass(object):
        return _old_getfile(object)
    
    # Lookup by parent module (as in current inspect)
    if hasattr(object, '__module__'):
        object_ = sys.modules.get(object.__module__)
        if hasattr(object_, '__file__'):
            return object_.__file__
    
    # If parent module is __main__, lookup by methods (NEW)
    for name, member in inspect.getmembers(object):
        if inspect.isfunction(member) and object.__qualname__ + '.' + member.__name__ == member.__qualname__:
            return inspect.getfile(member)
    else:
        raise TypeError('Source for {!r} not found'.format(object))

def pyprototyp(name="untitled", packages=[], useful=[], defs=[], classes=[]):
    """
    GIVEN:
    name    : string
    packages: list of strings
    useful  : list of strings
    defs    : list of defs (names NOT strings)
    classes : list of classes (names NOT strings)
    GET  : A .py file out, with desired defs & classes.
    """


    f = open(name + ".py", "w")

    ### upload required packages
    f.write("import numpy as np \n")
    for i in range(len(packages)):
        f.write(packages[i] + "\n")

    ### upload some useful stuff
    f.write("\n")
    f.write("π = np.pi \n")
    for i in range(len(useful)):
        f.write(useful[i] + "\n")

    ### upload custom classes & defintions
    f.write("\n")
    for i in range(len(defs)):
        string = inspect.getsource(defs[i])
        string = string.replace("", "")
        f.write(string + "\n")

    ### upload custom classes
    f.write("\n")
    for i in range(len(classes)):
        try:
            string = inspect.getsource(classes[i])
            string = string.replace("", "")
            f.write(string + "\n")
        except:
            obj = classes[i]
            cell_code = "".join(inspect.linecache.getlines(new_getfile(obj)))
            class_code = extract_symbols(cell_code, obj.__name__)[0][0]
            f.write(class_code + "\n")
    f.close()
    return None


