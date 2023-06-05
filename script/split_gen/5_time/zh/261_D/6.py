def main():
    n,m = map(int,input().split())
    x = list(map(int,input().split()))
    c = []
    y = []
    for i in range(m):
        c_i,y_i = map(int,input().split())
        c.append(c_i)
        y.append(y_i)
    print(n,m)
    print(x)
    print(c)
    print(y)
