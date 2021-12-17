

def read_input(name):
    with open(name,'r') as input:
        inp=input.readline()
    return inp

class Grid():
    def __init__(self):
        self.rows=1
        self.cols=1
        self.grid={
            -1: {-1:0, 0:0, 1:0},
             0: {-1:0, 0:1, 1:0},
             1: {-1:0, 0:0, 1:0}
        }

    def add_grid_col(self, col):
        for r in self.grid.keys():
            self.grid[r][-col]=0
            self.grid[r][col] =0
        self.cols+=1

    def add_grid_row(self, row):
        newRow={}
        for c in self.grid[0].keys():
            newRow[c]=0
        self.grid[-row]=newRow.copy()
        self.grid[row] =newRow.copy()
        self.rows+=1

    def show(self):
        print(" ", end=" | ")
        for c in sorted(self.grid[0]):
            print(f'{c:2d}', end=" | ")
        print()
        for r in sorted(self.grid, reverse=True):
            print(f'{r:2d}', end="  ")
            for c in sorted(self.grid[0]):
                print(f'{self.grid[r][c]:2d}', end="   ")
            print()

    def check_grid(self, pos):
        if (pos[1] > self.rows):
            self.add_grid_row(pos[1])
        elif (pos[1] < -self.rows):
            self.add_grid_row(pos[1])
        elif (pos[0] > self.cols):
            self.add_grid_col(pos[0])
        elif (pos[0] < -self.cols):
            self.add_grid_col(pos[0])
        else:
            pass

    def at(self, pos):
        return self.grid[pos[1]][pos[0]]

    def set(self, pos):
        self.grid[pos[1]][pos[0]] = 1

def take_command(curPos, command):
    if (command == "^"):   curPos=(curPos[0]  , curPos[1]+1)
    elif (command == "v"): curPos=(curPos[0]  , curPos[1]-1)
    elif (command == "<"): curPos=(curPos[0]-1, curPos[1])
    elif (command == ">"): curPos=(curPos[0]+1, curPos[1])
    else:
        print("Error!!")
        quit()
    return curPos

def p1():
    count=1
    curPos=(0,0)
    grid=Grid()

    inp = read_input("day03.dat")
    for command in inp:
        curPos=take_command(curPos, command)
        grid.check_grid(curPos)
        if grid.at(curPos)==0:
            count+=1
            grid.set(curPos)
    return count


def p2():
    count=1
    santaPos=(0,0)
    roboPos=(0,0)
    grid=Grid()

    inp = read_input("day03.dat")
    for n, command in enumerate(inp):
        if n%2==0:
            santaPos=take_command(santaPos, command)
            grid.check_grid(santaPos)
            if grid.at(santaPos)==0:
                count+=1
                grid.set(santaPos)
        else:
            roboPos=take_command(roboPos, command)
            grid.check_grid(roboPos)
            if grid.at(roboPos)==0:
                count+=1
                grid.set(roboPos)
                
    return count

def main():
    print(f"Part1: {p1()}")
    print(f"Part2: {p2()}")

if __name__ == "__main__":
  main()


