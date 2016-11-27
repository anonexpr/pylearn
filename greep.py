# grep -nr 

import os, re

icw = '/Users/ramaswamy.murugan/lpython/py3'
pattern = 'hello'

for root, directories, filenames in os.walk(icw):
    for filename in filenames:
           #print(filename)
           file_name = os.path.join(root,filename)
           f = open(file_name,'r')
           match = re.findall(pattern,f.read())
           if match:
              print(filename,' ',match)
            
