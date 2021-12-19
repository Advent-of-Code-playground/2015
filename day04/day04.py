import hashlib

def read_input(name):
    with open(name,'r') as input:
        inp=input.readline()
    return inp

def oldmd5(string):
    """ I still want to implement my own hash md5 calculator """
    return hashlib.md5(string.encode()).hexdigest()

def md5(string):
    """ I still want to implement my own hash md5 calculator """
    
    return hashlib.md5(string.encode()).hexdigest()

def p1():
    inp = read_input("day04.dat")

    for k in range(999999):
        hash = md5(inp+str(k))
        if hash[0:5] == "00000":
            break
    return k


def p2():
    inp = read_input("day04.dat")

    for k in range(99999999):
        hash = md5(inp+str(k))
        if hash[0:6] == "000000":
            break
    return k

def main():
    print(f"Part1: {p1()}")
    print(f"Part2: {p2()}")

if __name__ == "__main__":
  main()


