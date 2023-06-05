def main():
    n,m,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    ans=0
    time=0
    while time<=k:
        if len(a)==0 and len(b)==0:
            break
        elif len(a)==0:
            time+=b.pop(0)
            ans+=1
        elif len(b)==0:
            time+=a.pop(0)
            ans+=1
        elif a[0]<b[0]:
            time+=a.pop(0)
            ans+=1
        else:
            time+=b.pop(0)
            ans+=1
    print(ans-1)
