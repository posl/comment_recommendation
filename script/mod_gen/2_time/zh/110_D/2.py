def cal(n, m):
    if n == 1:
        return 1
    else:
        a = 0
        for i in range(1, m + 1):
            if m % i == 0:
                a += cal(n - 1, i)
        return a % (10 ** 9 + 7)
N, M = map(int, input().split())
print(cal(N, M))
