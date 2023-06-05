def solve():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    ans = "No"
    for i in range(2 ** n):
        sum = 0
        for j in range(n):
            if i >> j & 1 == 1:
                sum += a[j] * b[j]
        if sum == x:
            ans = "Yes"
            break
    print(ans)
solve()
