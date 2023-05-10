def problem179_c():
    n = int(input())
    ans = 0
    for i in range(1, n):
        for j in range(1, int(n/i)):
            if i * j + i == n:
                ans += 1
    print(ans)
