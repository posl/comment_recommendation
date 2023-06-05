def get_input():
    n = int(input())
    x = []
    y = []
    for i in range(0,n):
        line = input()
        x.append(int(line.split(" ")[0]))
        y.append(int(line.split(" ")[1]))
    return n,x,y
