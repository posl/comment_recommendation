def main():
    n,m = map(int,input().split())
    a = [0]*(n+1)
    for i in range(m):
        a[int(input())]=1
    a[0]=1
    a[1]=0
    for i in range(2,n+1):
        if a[i]==1:
            a[i]=0
        else:
            a[i]=a[i-1]+a[i-2]
            a[i]%=1000000007
    print(a[n])
