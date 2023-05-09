def main():
    n, x, y, z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [(a[i], b[i], a[i] + b[i], i + 1) for i in range(n)]
    c.sort(key=lambda x: (-x[0], x[3]))
    c.sort(key=lambda x: (-x[2], x[3]))
    c.sort(key=lambda x: (-x[1], x[3]))
    for i in range(x):
        print(c[i][3])
    for i in range(y):
        print(c[i + x][3])
    for i in range(z):
        print(c[i + x + y][3])

if __name__ == '__main__':
    main()