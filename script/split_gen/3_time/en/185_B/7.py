def problem185_b():
    n, m, t = map(int, input().split())
    a = []
    b = []
    for i in range(m):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    charge = n
    for i in range(m):
        if i == 0:
            charge -= a[i]
        else:
            charge -= a[i] - b[i-1]
        if charge <= 0:
            print("No")
            return
        charge += b[i] - a[i]
        if charge > n:
            charge = n
    charge -= t - b[m-1]
    if charge <= 0:
        print("No")
        return
    print("Yes")
