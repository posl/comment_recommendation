def main():
    n, m, t = map(int, input().split())
    a = [0] * (m + 1)
    b = [0] * (m + 1)
    for i in range(m):
        a[i], b[i] = map(int, input().split())
    a[m] = t
    b[m] = t
    charge = n
    for i in range(m + 1):
        charge -= a[i] - b[i - 1]
        if charge <= 0:
            print("No")
            return
        charge += a[i] - b[i - 1]
        if charge > n:
            charge = n
    print("Yes")

if __name__ == '__main__':
    main()