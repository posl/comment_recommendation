def solve():
    n, k = map(int, input().split())
    ans = 0
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            ans += int(str(i) + str(0) + str(j))
    print(ans)
