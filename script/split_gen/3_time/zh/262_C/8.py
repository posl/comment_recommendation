def problems262_c():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        if a[i] - 1 < n:
            b[a[i] - 1] = i
    ans = 0
    for i in range(n - 1):
        if b[i] > b[i + 1]:
            ans += 1
    print(ans * 2)
