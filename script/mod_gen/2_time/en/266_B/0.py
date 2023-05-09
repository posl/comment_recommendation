def main():
    n = int(input())
    x = 998244353 - abs(n) % 998244353
    if n < 0:
        x = 998244353 - x
    print(x)

if __name__ == '__main__':
    main()