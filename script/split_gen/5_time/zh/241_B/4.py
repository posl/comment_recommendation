def solve(n, m, a, b):
    if m > n:
        return False
    a.sort()
    b.sort()
    for i in range(m):
        if a[i] > b[i]:
            return False
    return True
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print('Yes' if solve(n, m, a, b) else 'No')
