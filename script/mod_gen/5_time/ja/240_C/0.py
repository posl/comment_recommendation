def main():
    n,x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai,bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    c = 0
    for i in range(n):
        if a[i] <= x:
            c += 1
            x -= a[i]
        else:
            break
    for i in range(n-c):
        x -= b[i+c]
    if x == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()