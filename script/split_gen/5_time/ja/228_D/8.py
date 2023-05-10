def solve():
    n = 1048576
    q = int(input())
    a = [-1 for _ in range(n)]
    for _ in range(q):
        t, x = map(int,input().split())
        if t == 1:
            h = x
            while a[h % n] != -1:
                h += 1
            a[h % n] = x
        else:
            print(a[x % n])
