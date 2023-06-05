def main():
    n,m = map(int,input().split())
    x = []
    y = []
    z = []
    for i in range(n):
        x1,y1,z1 = map(int,input().split())
        x.append(x1)
        y.append(y1)
        z.append(z1)
    # print(x)
    # print(y)
    # print(z)
    a = []
    for i in range(n):
        a.append(x[i]+y[i]+z[i])
    # print(a)
    a.sort(reverse=True)
    # print(a)
    print(sum(a[:m]))
