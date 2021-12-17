import re

def read_input(name):
    with open(name,'r') as input:
        inp=input.readlines()
    return inp

def test_string1(str):
    if test_prohibited(str): return False
    v = test_vowel(str)
    t = test_twice(str)
    if (v and t): return True
    else: return False

def test_vowel(str):
    return bool(len(re.findall(r'[aeiou]', str))>=3)

def test_twice(str):
    return bool(re.search(r'(?P<Name>[a-z])(?P=Name)', str))

def test_prohibited(str):
    return bool(re.search(r'ab|cd|pq|xy', str))

def p1():
    inp = read_input("day05.dat")
    nice=0
    for str in inp:
        if test_string1(str): 
            nice+=1
    return nice

def test_string2(str):
    d = test_double(str)
    m = test_middle(str)
    if (m and d): return True
    return False

def test_double(str):
    return bool(re.match(r'.*(?P<Name>[a-z]{2}).*(?P=Name)', str))

def test_middle(str):
    return bool(re.search(r'(?P<Name>[a-z]).(?P=Name)', str))

def p2():
    inp = read_input("day05.dat")
    nice=0
    for str in inp:
        
        if test_string2(str):
            print(f"{nice}: {str[:-1]}, {test_double(str)}, {test_middle(str)}")
            nice+=1
    return nice

def main():
    print(f"Part1: {p1()}")
    print(f"Part2: {p2()}")

if __name__ == "__main__":
  main()

