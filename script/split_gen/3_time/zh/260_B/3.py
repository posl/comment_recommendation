def main():
    n,x,y,z = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = []
    for i in range(n):
        c.append([a[i]+b[i],i+1])
    c.sort()
    c.reverse()
    for i in range(x):
        print(c[i][1])
    if y == 0:
        for i in range(x,x+z):
            print(c[i][1])
    else:
        for i in range(x,x+y):
            print(c[i][1])
        for i in range(x+y,x+y+z):
            print(c[i][1])
