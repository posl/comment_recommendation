def main():
    n, m, t = map(int, input().split())
    a = [0 for _ in range(m)]
    b = [0 for _ in range(m)]
    for i in range(m):
        a[i], b[i] = map(int, input().split())
    charge = n
    for i in range(m):
        charge -= a[i] - b[i - 1] if i > 0 else a[i]
        if charge <= 0:
            print("No")
            return
        charge += b[i] - a[i]
        charge = min(charge, n)
    charge -= t - b[-1]
    print("Yes" if charge > 0 else "No")
