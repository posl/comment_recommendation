def main():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    a=[x-1 for x in a]
    k-=1
    visited=[0]*n
    visited[0]=1
    now=0
    while k>0:
        if visited[a[now]]==1:
            break
        visited[a[now]]=1
        now=a[now]
        k-=1
    if k==0:
        print(now+1)
        return
    k%=visited[a[now]]-1
    now=a[now]
    while k>0:
        now=a[now]
        k-=1
    print(now+1)

if __name__ == '__main__':
    main()