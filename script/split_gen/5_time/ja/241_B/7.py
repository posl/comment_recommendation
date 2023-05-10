def check(n, m, a, b):
    if n < m:
        return False
    for i in range(m):
        if b[i] not in a:
            return False
    return True
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
