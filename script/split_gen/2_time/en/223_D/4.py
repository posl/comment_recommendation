def main():
    n,m = map(int,input().split())
    a = []
    b = []
    for i in range(m):
        c,d = map(int,input().split())
        a.append(c)
        b.append(d)
    a.sort()
    b.sort()
    if a[-1] > b[0]:
        print(-1)
    else:
        print(a[-1],b[0])
