from sys import argv

print('To Do List: '+' '.join(argv[1:]))

open('ToDo.txt', 'w+').write(' '.join(argv[1:]))
