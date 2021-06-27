import os

def read_input(name):
    with open(name,'r') as input:
        inp=input.readline()
    return inp



floor=0
first=True
inp=read_input('2015/day1.dat')
for pos, k in enumerate(inp):
    if k == '(': floor+=1
    elif k == ')': floor-=1
    else: print("Err")
    if floor == -1 and first:
        first = False
        firstMinus=pos+1

print(floor)
print(firstMinus)