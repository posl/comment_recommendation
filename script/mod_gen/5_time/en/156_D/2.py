def main():
    n, a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    if a + 1 == b:
        print(n * (n - 1) % 1000000007)
        return
    if a + 2 == b:
        print(n * (n - 1) % 1000000007 * (n - 2) % 1000000007)
        return
    print((n - a - 1) * (n - b - 1) % 1000000007)
main()

if __name__ == '__main__':
    main()