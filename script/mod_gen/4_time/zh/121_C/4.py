def main():
    n,m = map(int,input().split())
    num = 0
    sum = 0
    a = []
    b = []
    for i in range(n):
        x,y = map(int,input().split())
        a.append(x)
        b.append(y)
    while num < m:
        min = 1000000001
        for i in range(n):
            if min > a[i]:
                min = a[i]
                j = i
        if num + b[j] < m:
            sum += a[j] * b[j]
            num += b[j]
            a[j] = 1000000001
        else:
            sum += a[j] * (m - num)
            num = m
    print(sum)

if __name__ == '__main__':
    main()