def main():
    n, l = map(int, input().split())
    a = [l + i - 1 for i in range(1, n + 1)]
    b = [abs(i) for i in a]
    c = sum(a)
    d = b.index(min(b))
    print(c - a[d])

if __name__ == '__main__':
    main()