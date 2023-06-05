def problems200_c():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    mod = [0] * 200
    for i in range(n):
        mod[a[i] % 200] += 1
    for i in range(200):
        ans += mod[i] * (mod[i] - 1) // 2
    print(ans)
problems200_c()
