def get_input():
    input = raw_input()
    input = input.split()
    n = int(input[0])
    x = int(input[1])
    input = raw_input()
    input = input.split()
    l = map(int,input)
    return n,x,l
