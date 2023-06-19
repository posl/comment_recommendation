def main():
    n,m = [int(x) for x in input().split()]
    a = []
    b = []
    for i in range(n):
        a1,b1 = [int(x) for x in input().split()]
        a.append(a1)
        b.append(b1)
    # print(a)
    # print(b)
    # print(n,m)
    c = list(zip(a,b))
    # print(c)
    c.sort(key=lambda x:x[0])
    # print(c)
    sum = 0
    i = 0
    while m > 0:
        if m >= c[i][1]:
            sum += c[i][0] * c[i][1]
            m -= c[i][1]
        else:
            sum += c[i][0] * m
            m -= m
        i += 1
    print(sum)

if __name__ == '__main__':
    main()