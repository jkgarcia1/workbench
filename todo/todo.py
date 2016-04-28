#!/usr/bin/env python

from sys import argv
from os import system


# Extract the input arguments to form new todo item
text = ' '.join(argv[1:])[:80]
print('To Do List: ' + text)

# Append to file
f = 'ToDo.txt'
open(f, 'a').write(text+'\n')

# Show the items
print(open(f).read())

# Edit the items
system('e '+f)
