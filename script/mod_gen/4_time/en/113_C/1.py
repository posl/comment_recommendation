def main():
    n, m = map(int, input().split())
    p = [0] * m
    y = [0] * m
    for i in range(m):
        p[i], y[i] = map(int, input().split())
    print(p)
    print(y)
    return

if __name__ == '__main__':
    main()