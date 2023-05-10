def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    #print(a)
    #print(n,k)
    #print(a[n-1],a[0])
    if a[n-1]*a[0] >= 0:
        if k <= (n*(n-1))/2:
            print(a[0]*a[n-1])
        else:
            print(a[n-1]*a[0])
    else:
        if k <= (n*(n-1))/2:
            print(a[0]*a[n-1])
        else:
            print(a[n-1]*a[0])

if __name__ == '__main__':
    main()