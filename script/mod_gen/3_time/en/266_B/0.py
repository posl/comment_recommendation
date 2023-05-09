def main():
    N = int(input())
    if N > 0:
        print(N % 998244353)
    elif N < 0:
        print(998244353 + (N % 998244353))
    else:
        print(0)

if __name__ == '__main__':
    main()