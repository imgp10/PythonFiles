
import os      # imports os

print(os.getcwd())   # shows working directory

print(os.listdir(os.getcwd())) # shows folders within working directory

print(os.path.abspath('SCRIPT 2.pdf'))  # gives the path of the folder given in argument

os.path.isabs('')  # Tells whether path of file is absolute or not


import sys
file = str(sys.agrv[0]) # Gives the path of thefile currently in use


print(os.curdir) # gives current directory


print(os.path.dirname) # gives current directory

import os

print(dir(os))

