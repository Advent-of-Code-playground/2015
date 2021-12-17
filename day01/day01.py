

def read_input(name):
    with open(name,'r') as input:
        inp=input.readline()
    return inp

def process_position(pos):
    if pos == '(': return 1
    elif pos == ')': return -1
    else: 
        print("Err") 
        return 0

def p1():
    floor=0
    inp=read_input('day01.dat')
    for pos, k in enumerate(inp):
        floor += process_position(k)
    return floor

def p2():
    floor=0
    basement=False
    inp=read_input('day01.dat')
    for pos, k in enumerate(inp):
        floor += process_position(k)
        if (floor==-1): return pos+1

def main():
    print(f"Part1: {p1()}")
    print(f"Part2: {p2()}")

if __name__ == "__main__":
  main()


