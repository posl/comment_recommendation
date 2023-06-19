def solve():
    n, m, c = map(int, input().split())
    b_list = list(map(int, input().split()))
    a_list = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for a in a_list:
        sum = 0
        for i in range(m):
            sum += a[i] * b_list[i]
        if sum + c > 0:
            ans += 1
    print(ans)
solve()
