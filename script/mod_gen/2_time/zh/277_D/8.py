def main():
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    a.append(m)
    ans=0
    now=0
    for i in range(n):
        if a[i]==now:
            now+=1
        elif a[i]>now:
            ans+=a[i]-now
            now=a[i]+1
    print(ans)
main()
