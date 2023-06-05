def main():
    n, m, x, t, d = map(int, input().split())
    print(n, m, x, t, d)
    height = t
    for i in range(m, x):
        height += d
    print(height)
    for i in range(x, n):
        height += d
    print(height)

if __name__ == '__main__':
    main()