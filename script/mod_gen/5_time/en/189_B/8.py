def main():
    n, x = [int(i) for i in input().split()]
    v = []
    p = []
    for i in range(n):
        a, b = [int(i) for i in input().split()]
        v.append(a)
        p.append(b)
    total = 0
    for i in range(n):
        total += v[i] * p[i]
        if total > x * 100:
            print(i + 1)
            return
    print(-1)

if __name__ == '__main__':
    main()