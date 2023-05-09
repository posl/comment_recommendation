def main():
    n,k = map(int,input().split())
    while True:
        if n < k:
            break
        else:
            n = n % k
            if n == 0:
                break
            else:
                n = abs(n-k)
    print(n)

if __name__ == '__main__':
    main()