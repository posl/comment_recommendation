def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if n % (k - 1) == 0:
        print(n // (k - 1) - 1)
    else:
        print(n // (k - 1))

if __name__ == '__main__':
    main()