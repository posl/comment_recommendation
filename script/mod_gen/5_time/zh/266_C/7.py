def main():
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    d = list(map(int, input().split()))
    if a[0] < 0:
        a[0] = -a[0]
    if a[1] < 0:
        a[1] = -a[1]
    if b[0] < 0:
        b[0] = -b[0]
    if b[1] < 0:
        b[1] = -b[1]
    if c[0] < 0:
        c[0] = -c[0]
    if c[1] < 0:
        c[1] = -c[1]
    if d[0] < 0:
        d[0] = -d[0]
    if d[1] < 0:
        d[1] = -d[1]
    if a[0] > b[0] and a[0] > c[0] and a[0] > d[0] and a[1] > b[1] and a[1] > c[1] and a[1] > d[1]:
        print('Yes')
    elif b[0] > a[0] and b[0] > c[0] and b[0] > d[0] and b[1] > a[1] and b[1] > c[1] and b[1] > d[1]:
        print('Yes')
    elif c[0] > a[0] and c[0] > b[0] and c[0] > d[0] and c[1] > a[1] and c[1] > b[1] and c[1] > d[1]:
        print('Yes')
    elif d[0] > a[0] and d[0] > b[0] and d[0] > c[0] and d[1] > a[1] and d[1] > b[1] and d[1] > c[1]:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()