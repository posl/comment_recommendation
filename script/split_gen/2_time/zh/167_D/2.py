def solve(n, k, a):
    k = k % n
    for i in range(k):
        a = a[a-1]
    return a
n, k = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, k, a))
