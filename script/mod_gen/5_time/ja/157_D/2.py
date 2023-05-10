def main():
    n, m, k = map(int, input().split())
    a = [0] * n
    b = [0] * n
    for i in range(m):
        ai, bi = map(int, input().split())
        a[ai - 1] += 1
        b[bi - 1] += 1
    c = [0] * n
    d = [0] * n
    for i in range(k):
        ci, di = map(int, input().split())
        c[ci - 1] += 1
        d[di - 1] += 1
    for i in range(n):
        print(a[i] - c[i] - 1, end=' ')
    print()

if __name__ == '__main__':
    main()