def main():
    n,c = map(int,input().split())
    a = []
    b = []
    d = []
    for i in range(n):
        ai,bi,ci = map(int,input().split())
        a.append(ai)
        b.append(bi)
        d.append(ci)
    sum = 0
    for i in range(n):
        sum += d[i] * (b[i] - a[i] + 1)
    if sum < c:
        print(sum)
    else:
        print(c)

if __name__ == '__main__':
    main()