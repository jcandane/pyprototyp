# pyprototyp
Using Jupyter Notebooks to Draft Py files

GIVEN:

name    : string  
packages: list of strings  
useful  : list of strings  
defs    : list of defs (names NOT strings)  
classes : list of classes (names NOT strings)  

GET  : A .py file out, with desired defs & classes.

Add to the last line in Jupyter Notebooks to export a trimed python file. 
Just include:

```
!git clone https://github.com/jcandane/pyprototyp
from pyprototyp.pyprototyp import pyprototyp
pyprototyp("filename.py", packages=[], useful=[], defs=[], classes=[])
```

