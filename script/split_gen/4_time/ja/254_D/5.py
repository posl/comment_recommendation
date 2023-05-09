def solve():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i*j <= n and (i*j)**0.5 == int((i*j)**0.5):
                ans += 1
    print(ans)
