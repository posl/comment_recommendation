def solve():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    sum_a = sum(a)
    t %= sum_a
    for i in range(n):
        if t < a[i]:
            print(i + 1, t)
            break
        t -= a[i]
solve()
