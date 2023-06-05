def main():
    n,k = list(map(int, input().split()))
    if n < k:
        print(n)
    else:
        print(min(n % k, k - n % k))

if __name__ == '__main__':
    main()