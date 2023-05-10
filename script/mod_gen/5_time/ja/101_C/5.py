def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    min_a = min(a)
    if min_a == 1:
        if n%k == 0:
            print(n//k)
        else:
            print(n//k+1)
    else:
        if (n-1)%(k-1) == 0:
            print((n-1)//(k-1))
        else:
            print((n-1)//(k-1)+1)
main()

if __name__ == '__main__':
    main()