def main():
    n, k = [int(x) for x in input().split()]
    print(min(n % k, k - n % k))

if __name__ == '__main__':
    main()