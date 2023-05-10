def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    s = 0
    for i in range(n):
        s += a[i]/b[i]
    s /= 2
    t = 0
    for i in range(n-1, -1, -1):
        if s >= a[i]/b[i]:
            t += a[i]
            s -= a[i]/b[i]
        else:
            t += s*b[i]
            break
    print(t)
main()

if __name__ == '__main__':
    main()