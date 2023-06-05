def solve():
    # 读取输入
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    # 从c中读取出b
    b = [0] * (m + 1)
    for i in range(n + m):
        b[m - i] = c[i] // a[n]
        # 用b更新c
        for j in range(n + 1):
            c[i + j] -= b[m - i] * a[n - j]
    for i in range(m + 1):
        print(b[i], end=' ')
    print()
