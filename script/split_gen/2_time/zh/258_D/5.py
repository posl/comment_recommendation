def main():
    n,x = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        ai,bi = map(int,input().split())
        a.append(ai)
        b.append(bi)
    res = 0
    for i in range(n):
        res += a[i] + b[i]
    if res <= x:
        print(res)
    else:
        res = 0
        for i in range(n):
            res += a[i]
            if res > x:
                print(i)
                return
        print(n)
main()
