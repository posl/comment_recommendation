def main():
    n, a, b = map(int, input().split())
    q, mod = divmod(n, a + b)
    print(q * a + min(a, mod))

if __name__ == '__main__':
    main()