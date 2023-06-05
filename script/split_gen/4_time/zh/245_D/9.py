def solve():
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    b = [0] * (M + 1)
    b[0] = c[0] // a[0]
    for i in range(1, M + 1):
        b[i] = (c[i] - sum([b[j] * a[i - j] for j in range(i)])) // a[0]
    print(*b[::-1])
solve()
