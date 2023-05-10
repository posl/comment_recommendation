def main():
    n, k = [int(i) for i in input().split()]
    while n >= k:
        n = n % k
        if n == 0:
            print(0)
            return
    print(min(n, abs(n-k)))

if __name__ == '__main__':
    main()