"""
#module/modules :

-It is a simple python file
-A file with an extension like '.py' is one module.
-module = File
-----------------------------------------
-There are 2 Types of modules which are,
 1. Built-in modules    2. User defined modules
======================================

#1. Built in modules :
- The modules which are present/given by python itself
 are called as Built-in modules.
- In order to check Built-in modules use,
    #print(help('modules'))
- It will return the modules/files having extension like .py
  which are present or available on your Machine .
------------------------------------------
use math module for example,
syntax: import module_name
---------
Examples:
1- import math
print(math.pi)
print(math.sqrt(625))
print(math.sin(90))
 output is:
3.141592653589793
25.0
0.8939966636005579

Process finished with exit code 0
# module importing is important to access
  members of that particular file
------------------------------
# Use module aliasing : which means assign a
  nike name for that particular module you
  want to access or import.
like,
import math as m
print(m.sqrt(1000))

output is:
31.622776601683793

Process finished with exit code 0
-----------------------------------
- If we want all the members to be accessible
  directly in the env., then use 'from .... import' option
# syntax : from module_name import all *
example:
from math import *
- it will give all the methods present in the math module
# ' * ' means everything/all members.
from math import *
print(pi)
print(e, sqrt(121), sin(45))
---------------------------
# member aliasing:
ex.
from math import factorial as f
f(24)
print(f(4))
output is:
24

Process finished with exit code 0
======================================
RECAP
import math
import math as m
from math import *
from math import sin,sqrt,e,pi
from math import factorial as f
----------------------------
# some important built-in modules:
array
time
sys
os
collection
itertools
random
statistics




"""




