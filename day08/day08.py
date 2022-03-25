import re

def read_input(name):
    with open(name,'r') as input:
        inp=input.readline()
    return inp

def process_string(string):
    codeSize=len(string)
    memoSize=len(string)
    pass

def p1():
    # string="hrhqqxow\xe2gsydtdspcfqy\"zw\\ou"
    string='\xe2\"\\'
    string=string.encode("raw_unicode_escape")
    print(string,":" ,  len(string))
    quote=re.findall(r"\"", string)
    print(quote)
    bar=re.findall(r"\\\\", string)
    print(bar)
    hexa=re.findall(r"\\xe2", string)
    print(hexa)



def p2():
    pass

def main():
    print(f"Part1: {p1()}")
    print(f"Part2: {p2()}")

if __name__ == "__main__":
  main()


