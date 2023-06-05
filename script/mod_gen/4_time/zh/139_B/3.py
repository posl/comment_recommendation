def solve():
    a,b = map(int,input().split())
    c = 1
    while a < b:
        a += a-1
        c += 1
    print(c)
solve()
