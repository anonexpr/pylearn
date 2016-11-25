#get the current working directory

import os

print(os.getcwd())

# get filename and path
pathname = '/Users/ramaswamy.murugan/non-work/GITHUB/pylearn/README.md'
#print(os.path.split(pathname))
filename = os.path.split(pathname)[1]
dirname = os.path.split(pathname)[0]
print(filename)
print(dirname)

# construct absolute path names
print(os.path.realpath('README.MD'))
