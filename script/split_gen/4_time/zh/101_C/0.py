def main():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    ans=0
    for i in range(n-k):
        if a[i]>=a[i+k]:
            ans+=1
    print(ans)
