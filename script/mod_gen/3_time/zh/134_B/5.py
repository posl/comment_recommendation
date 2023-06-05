def main():
    n, d = map(int, input().split())
    print(n // (2*d + 1) + (1 if n % (2*d + 1) > 0 else 0))

if __name__ == '__main__':
    main()