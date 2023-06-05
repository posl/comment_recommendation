def solve():
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    total = sum(a)
    k = (x // total) * n
    x %= total
    for i in range(n):
        if x < 0:
            break
        x -= a[i]
        k += 1
    print(k)
solve()
