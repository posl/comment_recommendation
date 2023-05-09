def solve():
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    d = 0
    for i in range(n):
        d += l[i]
        if d > x:
            print(i + 1)
            return
    print(n + 1)
