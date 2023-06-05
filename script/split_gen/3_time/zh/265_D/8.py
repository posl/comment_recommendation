def main():
    n,p,q,r=map(int,input().split())
    a=list(map(int,input().split()))
    maxa=[0]*n
    maxa[-1]=a[-1]
    for i in range(n-2,-1,-1):
        maxa[i]=max(maxa[i+1],a[i])
    mina=[0]*n
    mina[-1]=a[-1]
    for i in range(n-2,-1,-1):
        mina[i]=min(mina[i+1],a[i])
    for i in range(n):
        if mina[i]<=p and maxa[i]>=p and mina[i]<=q-p and maxa[i]>=q-p and mina[i]<=r-q+p and maxa[i]>=r-q+p:
            print("Yes")
            return
    print("No")
