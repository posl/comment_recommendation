def main():
    n, m, t = map(int, input().split())
    a = []
    b = []
    for i in range(m):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    charge = n
    prev = 0
    for i in range(m):
        charge -= a[i] - prev
        if charge <= 0:
            print("No")
            return
        charge += b[i] - a[i]
        if charge >= n:
            charge = n
        prev = b[i]
    charge -= t - prev
    if charge <= 0:
        print("No")
    else:
        print("Yes")
