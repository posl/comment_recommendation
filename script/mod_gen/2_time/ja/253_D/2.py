def main():
    n, a, b = map(int, input().split())
    c = n // a + n // b
    d = n // (a * b)
    print(n * (n + 1) // 2 - c * (c + 1) // 2 + d * (d + 1) // 2)

if __name__ == '__main__':
    main()