def f(n, m, i, a):
    if i == n:
        print(*a)
    else:
        for j in range(1, m+1):
            if i == 0 or a[i-1] < j:
                a[i] = j
                f(n, m, i+1, a)
n, m = map(int, input().split())
a = [0]*n
f(n, m, 0, a)
