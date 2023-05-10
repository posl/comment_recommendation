def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    res = 0
    for i in range(n):
        res += a[i] * b[i]
        if res > x * 100:
            print('No')
            return
    if res < x:
        print('No')
    else:
        print('Yes')
main()

if __name__ == '__main__':
    main()