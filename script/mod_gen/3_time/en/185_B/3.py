def main():
    n, m, t = map(int, input().split())
    a = []
    b = []
    for i in range(m):
        a1, b1 = map(int, input().split())
        a.append(a1)
        b.append(b1)
    charge = n
    prev_time = 0
    for i in range(m):
        charge -= a[i] - prev_time
        if charge <= 0:
            print("No")
            exit()
        charge += b[i] - a[i]
        if charge > n:
            charge = n
        prev_time = b[i]
    charge -= t - prev_time
    if charge <= 0:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()