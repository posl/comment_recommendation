def main():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    xy=[list(map(int,input().split())) for _ in range(n)]
    xy=sorted(xy,key=lambda x:x[0]**2+x[1]**2)
    ans=0
    for i in range(k):
        ans=max(ans,xy[a[i]-1][0]**2+xy[a[i]-1][1]**2)
    print(ans**0.5)
main()
