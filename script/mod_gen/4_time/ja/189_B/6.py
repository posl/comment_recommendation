def main():
    n, x = map(int, input().split())
    v = []
    p = []
    for _ in range(n):
        a, b = map(int, input().split())
        v.append(a)
        p.append(b)
    total = 0
    for i in range(n):
        total += v[i] * p[i]
        if total > x * 100:
            print(i + 1)
            return
    print(-1)
main()

if __name__ == '__main__':
    main()