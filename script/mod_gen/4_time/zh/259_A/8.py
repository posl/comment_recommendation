def main():
    n, m, x, t, d = map(int, input().split())
    height = t
    for i in range(1, x):
        height += d
    for i in range(x, m):
        height += d
    print(height)

if __name__ == '__main__':
    main()