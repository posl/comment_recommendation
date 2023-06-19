def main():
    n = int(input())
    if n < 0:
        n = -n
        n = n % 998244353
        n = 998244353 - n
    else:
        n = n % 998244353
    print(n)

if __name__ == '__main__':
    main()