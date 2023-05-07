def main():
    n, m, t = map(int, input().split())
    a = [0] * m
    b = [0] * m
    for i in range(m):
        a[i], b[i] = map(int, input().split())
    charge = n
    for i in range(m):
        if i == 0:
            charge -= a[i]
        else:
            charge -= a[i] - b[i - 1]
        if charge <= 0:
            print('No')
            return
        charge = min(charge + b[i] - a[i], n)
    charge -= t - b[m - 1]
    if charge <= 0:
        print('No')
    else:
        print('Yes')
