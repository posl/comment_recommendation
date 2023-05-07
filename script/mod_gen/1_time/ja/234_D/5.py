def main():
    n,k=map(int,input().split())
    p=list(map(int,input().split()))
    c=[0]*(n+1)
    for i in range(n):
        c[p[i]]=i
    ans=[0]*n
    for i in range(n):
        ans[i]=c[i+1]
    ans.sort()
    for i in range(k):
        print(0)
    for i in range(k,n):
        print(ans[i]-ans[i-1])

if __name__ == '__main__':
    main()