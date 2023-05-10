def problem():
    n = int(input())
    cnt = 0
    for i in range(1, n+1):
        for j in range(i, n+1):
            if i*j <= n and i != j:
                cnt += 2
            elif i*j <= n and i == j:
                cnt += 1
    print(cnt)
