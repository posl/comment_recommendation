def solve():
    n = int(input())
    v = list(map(int, input().split()))
    ans = 0
    for i in range(0, n, 2):
        if v[i] == v[i+1]:
            ans += 1
    print(ans)
solve()
