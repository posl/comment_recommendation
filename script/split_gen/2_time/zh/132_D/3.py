def count_kinds(n, k):
    if k > n//2:
        k = n - k
    if k == 1:
        return n - 1
    if k == 2:
        return n * (n - 1) // 2
    if k == 3:
        return n * (n - 1) * (n - 2) // 6
n, k = map(int, input().split())
