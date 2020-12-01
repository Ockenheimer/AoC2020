import fileinput
from typing import List

file = open('inputDec01', mode='r')

s: list[str] = file.readlines()

for x in s:
    x1 = int(x.rstrip("\n"))
    for y in s:
        y1 = int(y.rstrip("\n"))
        if x1 + y1 == 2020:
            print(x1 * y1)

file.close()