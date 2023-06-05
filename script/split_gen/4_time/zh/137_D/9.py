def main():
    n,m = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        a1,b1 = map(int,input().split())
        a.append(a1)
        b.append(b1)
    a1 = []
    b1 = []
    for i in range(n):
        if a[i] <= m:
            a1.append(a[i])
            b1.append(b[i])
    if len(a1) == 0:
        print(0)
    else:
        print(max(b1))
