def main():
    n,m = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a1,b1 = map(int, input().split())
        a.append(a1)
        b.append(b1)
    min = 0
    sum = 0
    for i in range(n):
        min += a[i] * b[i]
        sum += b[i]
    if sum == m:
        print(min)
    elif sum > m:
        for i in range(n):
            if b[i] > m:
                min -= a[i] * b[i]
                min += a[i] * m
                print(min)
                break
            elif b[i] == m:
                min -= a[i] * b[i]
                min += a[i] * m
                print(min)
                break
            else:
                min -= a[i] * b[i]
                m -= b[i]
    else:
        print(min)

if __name__ == '__main__':
    main()