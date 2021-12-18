

def read_input(name):
    inp=[]
    with open(name,'r') as input:
        rawInp = input.readlines()
        for line in rawInp:
            inp.append(line.split())
    return inp

class Grid():
    def __init__(self, size):
        self.grid=[]
        for i in range(size):
            self.grid.append([])
            for j in range(size):
                self.grid[i].append(0)



    def on1(self, p1, p2):
        x1, y1, x2, y2 = p1[0], p1[1], p2[0], p2[1]
        for i in range(x1, x2+1):
            for j in range(y1,y2+1):
                self.grid[i][j]=1

    def off1(self, p1, p2):
        x1, y1, x2, y2 = p1[0], p1[1], p2[0], p2[1]
        for i in range(x1, x2+1):
            for j in range(y1,y2+1):
                self.grid[i][j]=0

    def toggle1(self, p1, p2):
        x1, y1, x2, y2 = p1[0], p1[1], p2[0], p2[1]
        for i in range(x1, x2+1):
            for j in range(y1,y2+1):
                self.grid[i][j]=abs(self.grid[i][j]-1)

    def on2(self, p1, p2):
        x1, y1, x2, y2 = p1[0], p1[1], p2[0], p2[1]
        for i in range(x1, x2+1):
            for j in range(y1,y2+1):
                self.grid[i][j]+=1

    def off2(self, p1, p2):
        x1, y1, x2, y2 = p1[0], p1[1], p2[0], p2[1]
        for i in range(x1, x2+1):
            for j in range(y1,y2+1):
                self.grid[i][j]-=1
                if self.grid[i][j] < 0: 
                    self.grid[i][j]=0

    def toggle2(self, p1, p2):
        x1, y1, x2, y2 = p1[0], p1[1], p2[0], p2[1]
        for i in range(x1, x2+1):
            for j in range(y1,y2+1):
                self.grid[i][j]+=2

    def getLit(self):
        count=0
        for line in self.grid:
            for lamp in line:
                count+=lamp
        return count

    def show(self):
        for i in self.grid:
            print(i)
 
def p1():
    inp = read_input("day06.dat")
    grid=Grid(1000)
    for line in inp:
        cmd=line[0]
        p1=list(map(int, line[-3].split(",")))
        p2=list(map(int, line[-1].split(",")))
        if cmd == "turn":
            opt=line[1]
            if opt == "on":
                grid.on1(p1, p2)
            elif opt == "off":
                grid.off1(p1,p2)
        elif cmd == "toggle":
            grid.toggle1(p1,p2)
    return grid.getLit()

def p2():
    inp = read_input("day06.dat")
    grid=Grid(1000)
    for line in inp:
        cmd=line[0]
        p1=list(map(int, line[-3].split(",")))
        p2=list(map(int, line[-1].split(",")))
        if cmd == "turn":
            opt=line[1]
            if opt == "on":
                grid.on2(p1, p2)
            elif opt == "off":
                grid.off2(p1,p2)
        elif cmd == "toggle":
            grid.toggle2(p1,p2)
    return grid.getLit()

def main():
    print(f"Part1: {p1()}")
    print(f"Part2: {p2()}")

if __name__ == "__main__":
  main()


