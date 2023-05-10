def main():
    x = []
    y = []
    for i in range(4):
        a,b = map(int,input().split())
        x.append(a)
        y.append(b)
    if (x[1]-x[0])*(y[2]-y[1]) == (x[2]-x[1])*(y[1]-y[0]):
        print("No")
    else:
        print("Yes")
