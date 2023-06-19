def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    #print(a)
    #print(n,k)
    #print(a)
    #print(a[0])
    #print(a[n-1])
    #print(k//n)
    #print(k%n)
    for i in range(n):
        print(k//n+1 if a[i] <= k%n else k//n)

if __name__ == '__main__':
    main()