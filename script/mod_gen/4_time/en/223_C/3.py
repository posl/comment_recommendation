def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    t = 0
    for i in range(n):
        t += a[i] / b[i]
    t /= 2
    d = 0
    for i in range(n):
        if t >= a[i] / b[i]:
            d += a[i]
        else:
            d += b[i] * t
    print(d)

if __name__ == '__main__':
    main()