def main():
    n, m, t = map(int, input().split())
    a = []
    b = []
    for i in range(m):
        a_temp, b_temp = map(int, input().split())
        a.append(a_temp)
        b.append(b_temp)
    charge = n
    for i in range(m):
        if i == 0:
            charge -= a[i]
        else:
            charge -= a[i] - b[i-1]
        if charge <= 0:
            print('No')
            return
        charge += b[i] - a[i]
        if charge > n:
            charge = n
    charge -= t - b[-1]
    if charge <= 0:
        print('No')
    else:
        print('Yes')

if __name__ == '__main__':
    main()