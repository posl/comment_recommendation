def f(n, k):
    if k == 0 or k == n:
        return 1
    return f(n-1, k-1) + f(n-1, k)
h, w, k = map(int, input().split())
print(f(h, k-1) * f(h+1, w-k) % 1000000007)
