def solve():
    n, m, t = map(int, input().split())
    a = [0] * m
    b = [0] * m
    for i in range(m):
        a[i], b[i] = map(int, input().split())
    charge = n
    prev = 0
    for i in range(m):
        charge -= a[i] - prev
        if charge <= 0:
            return False
        charge = min(n, charge + b[i] - a[i])
        prev = b[i]
    charge -= t - prev
    return charge > 0
print("Yes" if solve() else "No")
