def main():
    n=int(input())
    a=list(map(int,input().split()))
    ans=0
    for i in range(n):
        for j in range(i,n):
            x=0
            for k in range(i,j+1):
                x|=a[k]
            ans^=x
    print(ans)
main()
