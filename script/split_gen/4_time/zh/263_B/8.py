def problem263_b():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        x = i + 1
        while x != 1:
            x = p[x - 2]
            ans += 1
    print(ans)
problem263_b()
