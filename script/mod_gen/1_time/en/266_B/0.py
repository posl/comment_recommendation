def main():
    N = int(input())
    if N >= 0:
        print(N % 998244353)
    else:
        print(998244353 - (-N % 998244353))

if __name__ == '__main__':
    main()