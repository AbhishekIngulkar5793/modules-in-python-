"""
2. user defined module:
- A module or a python file created by a user is called as
  user defined module
# Example:
create a test.py in project dir.
and import it into modules_m2_day_24.py
------------------------------
#1
import test
print(test.x, test.y, test.z)

output is:
ganesh 66.88 python

Process finished with exit code 0
#2. module aliasing
import test as t
print(t.bank_name)

output is:
SBI

Process finished with exit code 0
#3 import all members directly
from test import *
print(x)

output is:
ganesh

Process finished with exit code 0
#4 import only the specific members
from test import x,z
print(x, z)
output is:
ganesh python

Process finished with exit code 0
======================================
# module importing makes a code concise
# it gives an access to the members of other
 module just by writing a single line
-------------------------
#5. member aliasing
from test import bank_name as bnm
print(bnm)
output is:
SBI

Process finished with exit code 0
------------------------------------
import test
- you will get the module only if:
1. If the module is present in project directory
2. or If it is present in python default directory
# otherwise you cannot import the module/file, it will
return an error.
# python is a case sensitive language, hence while
 importing modules you need to take care.
-------------------------------------
# If your module is present in the sub_directory
 then first access that directory and then only
  you can access modules present in it
# take a help of from .... import
example:
# create a bank dir ==> create insurance dir. ==> create
  setup.py
# from setup.py access amount value
from bank.insurance import setup
print(setup.amt)

output is:
456456456

Process finished with exit code 0
-----------------------------------
from bank.insurance.setup import amt
print(amt)
output is:
456456456

Process finished with exit code 0
-------------------------------
from bank.account import IFSC
print(IFSC)
output is:
SBI230

Process finished with exit code 0
---------------------------
from new_folder.test import x,y,z
print(x, y, z)
output is:
ganesh 66.88 python

Process finished with exit code 0


"""
