def main():
    n,m,x = map(int,input().split())
    c = []
    a = []
    for i in range(n):
        c.append(list(map(int,input().split())))
    for i in range(n):
        a.append(c[i][1:])
    print(c)
    print(a)
    print(n,m,x)
