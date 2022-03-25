

def read_input(name):
    inp=[]
    with open(name,'r') as input:
        rawInp=input.readlines()
        for line in rawInp:
            inp.append(line.split("->"))
    return inp

class Wire():
    def __init__(self):
        self.signalIN=0
        self.connection={}

    def setSignalIn(self, signal):
        pass
    
    def createConnection(self, gate, outWire):
        pass

    def getSignal(self):
        pass

class Gate():
    def __init__(self, type, wireOUT):
        self.type=""
        self.wireOUT=wireOUT
    
    def evalGate(self):
        pass

def process_command(line):
    if ("NOT" in line):
        gate="NOT"
        wireIN=line[0].split()[-1]
        wireOUT=line[1].strip()
        return wireIN, gate, wireOUT
    elif ("LSHIFT" in line):
        gate="LSHIFT"
        wireIN=line[0].split()[0]
        shift=line[2].split()[0]
        wireOUT=line[1].strip()
        return wireIN, gate, shift, wireOUT
    elif ("RSHIFT" in line):
        gate="RSHIFT"
        wireIN=line[0].split()[0]
        shift=line[2].split()[0]
        wireOUT=line[1].strip()
        return wireIN, gate, shift, wireOUT
    elif ("AND" in line):
        gate="AND"
        wireIN1=line[0].split()[0]
        wireIN2=line[0].split()[2]
        wireOUT=line[1].strip()
        return wireIN1, wireIN2, gate, wireOUT
    elif ("OR" in line):
        gate="OR"
        wireIN1=line[0].split()[0]
        wireIN2=line[0].split()[2]
        wireOUT=line[1].strip()
        return wireIN1, wireIN2, gate, wireOUT
    else:
        n=line[0].strip()
        wireOUT=line[1].strip()
        return n, wireOUT

def p1():
    inp = read_input("day07.dat")
    print(inp[2][0].split())
    wires={}
    print(hex(0x01 or 0x10))
    


def p2():
    pass

def main():
    print(f"Part1: {p1()}")
    print(f"Part2: {p2()}")

if __name__ == "__main__":
  main()


