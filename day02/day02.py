

def read_input(name):
    with open(name,'r') as input:
        inp=input.readlines()
    return inp

def p1():
    total_wrapper=0
    inp=read_input("day02.dat")
    for present in inp:
        box=[int(x) for x in present.split("x")]
        box.sort()
        l, w, h = box[0], box[1], box[2]
        wrapper=2*(l*w) + 2*(w*h) + 2*(h*l)
        total_wrapper+=wrapper + (l*w)
    return total_wrapper

def p2():
    total_ribbon=0
    inp=read_input("day02.dat")
    for present in inp:
        box=[int(x) for x in present.split("x")]
        box.sort()
        l, w, h = box[0], box[1], box[2]
        ribbon=2*l + 2*w
        total_ribbon += ribbon + (l*w*h)
    return total_ribbon

def main():
    print(f"Part1: {p1()}")
    print(f"Part2: {p2()}")

if __name__ == "__main__":
  main()


