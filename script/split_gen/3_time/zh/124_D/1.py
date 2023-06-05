def main():
    n,k=map(int,input().split())
    s=input()
    ans=0
    for i in range(n):
        if s[i]=='0':
            ans+=1
    if ans==n:
        print(n)
        return
    tmp=0
    for i in range(k):
        if s[i]=='0':
            tmp+=1
    ans=max(ans,tmp)
    for i in range(k,n):
        if s[i-k]=='0':
            tmp-=1
        if s[i]=='0':
            tmp+=1
        ans=max(ans,tmp)
    print(ans)
    return
