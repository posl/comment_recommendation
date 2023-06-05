def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    for i in range(1, 1001):
        ok = True
        for j in range(n):
            if not (a[j] <= i <= b[j]):
                ok = False
        if ok:
            ans += 1
    print(ans)
solve()
