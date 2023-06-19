def main():
    x,k = map(int,input().split())
    i = 0
    while i < k:
        x = x + 5 - x % 10 if x % (10 ** (i + 1)) >= 5 * 10 ** i else x - x % 10
        i += 1
    print(x)

if __name__ == '__main__':
    main()