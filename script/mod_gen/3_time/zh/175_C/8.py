def main():
    x, k, d = map(int, input().split())
    x = abs(x)
    if k*d <= x:
        print(x-k*d)
        return
    if (k*d - x) % (2*d) == 0:
        print(0)
        return
    print(min(abs(x + d * (k - 2 * (x // d + 1))), abs(x - d * (k - 2 * (x // d + 1)))))

if __name__ == '__main__':
    main()