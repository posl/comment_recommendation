def main():
    n, x = map(int, input().split())
    v = []
    p = []
    for i in range(n):
        a, b = map(int, input().split())
        v.append(a)
        p.append(b)
    s = 0
    for i in range(n):
        s += v[i] * p[i] / 100
        if s > x:
            print(i + 1)
            break
    else:
        print(-1)

if __name__ == '__main__':
    main()