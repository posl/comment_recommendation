def problems200_c():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [0] * 200
    for i in range(n):
        b[a[i] % 200] += 1
    ans = 0
    for i in range(200):
        ans += b[i] * (b[i] - 1) // 2
    print(ans)
    return
problems200_c()
