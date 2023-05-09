def main():
    n,k = map(int, input().split())
    if n == 0:
        print(0)
        return
    if k == 1:
        print(0)
        return
    if n < k:
        print(n)
        return
    r = n % k
    print(min(r,abs(r-k)))

if __name__ == '__main__':
    main()