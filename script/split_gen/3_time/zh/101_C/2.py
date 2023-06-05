def main():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    if k==1:
        print(0)
        return
    ans=0
    for i in range(n-k+1):
        if a[i+k-1]==min(a[i:i+k]):
            ans+=1
    print(ans)
