def main():
    n, m, x, t, d = map(int, input().split())
    h = t
    for i in range(1, x):
        h += d
    for i in range(x, m):
        h += d
    for i in range(m, n):
        h += d
    print(h)

if __name__ == '__main__':
    main()