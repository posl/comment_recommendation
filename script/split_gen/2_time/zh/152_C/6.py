def solve():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    min_p = n + 1
    for i in range(n):
        if p[i] <= min_p:
            min_p = p[i]
            ans += 1
    print(ans)
