def main():
    n, m, x, t, d = map(int, input().split())
    h = t
    for i in range(x, n):
        h += d
    for i in range(x, m):
        h -= d
    print(h)

if __name__ == '__main__':
    main()