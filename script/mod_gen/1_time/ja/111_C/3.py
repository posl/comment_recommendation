def main():
    n = int(input())
    v = list(map(int, input().split()))
    if n == 2:
        print(0)
        return
    a = v[0::2]
    b = v[1::2]
    a.sort()
    b.sort()
    c = a[0]
    d = b[0]
    e = a[-1]
    f = b[-1]
    if c == e and d == f:
        print(n - max(a.count(c), b.count(d)))
    elif c == e:
        print(n - a.count(c))
    elif d == f:
        print(n - b.count(d))
    else:
        print(n - a.count(c) - b.count(d))

if __name__ == '__main__':
    main()