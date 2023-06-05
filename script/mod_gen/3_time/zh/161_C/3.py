def main():
    n,k = map(int,input().split())
    while True:
        if n > k:
            n = n%k
        else:
            break
    print(min(n,abs(n-k)))

if __name__ == '__main__':
    main()