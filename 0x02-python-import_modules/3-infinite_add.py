#!/usr/bin/python3
from sys import argv
add = 0
for i in argv[1:]:
    add += int(i)
print("{:d}".format(add))
