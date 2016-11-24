#Check for existence of a file

import os

if os.path.isfile('/etc/passw'):
   print('file exists')
else:
   print('file does not exist')
