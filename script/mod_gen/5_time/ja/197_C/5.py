def main():
    n=int(input())
    a=list(map(int,input().split()))
    ans=0
    for i in range(n):
        for j in range(i,n):
            tmp=0
            for k in range(i,j+1):
                tmp|=a[k]
            ans^=tmp
    print(ans)
main()
