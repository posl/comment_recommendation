def main():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    a1=a[0]
    a2=a[1]
    if k>=n:
        for i in range(n):
            print(k//n)
    else:
        k1=k
        for i in range(n):
            if a[i]==a1:
                print(k1//n+1)
                k1-=1
            else:
                print(k1//n)

if __name__ == '__main__':
    main()