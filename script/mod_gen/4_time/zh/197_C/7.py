def main():
    n=int(input())
    a=list(map(int,input().split()))
    min_xor=2**31-1
    for i in range(2**(n-1)):
        xor=a[0]
        ors=a[0]
        for j in range(1,n):
            if i & 2**(j-1):
                xor^=a[j]
                ors|=a[j]
            else:
                xor=a[j]
                ors=a[j]
        min_xor=min(min_xor,xor)
    print(min_xor)

if __name__ == '__main__':
    main()