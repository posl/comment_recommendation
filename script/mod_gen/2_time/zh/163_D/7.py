def func(n, k):
    if k == 1:
        return n
    elif k == n + 1:
        return 1
    else:
        return n * (n + 1) // 2 - k + 1
n, k = map(int, input().split())
print(func(n, k) % (10 ** 9 + 7))
