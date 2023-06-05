def solve():
    N,K=map(int,input().split())
    ans=0
    for i in range(1,N+1):
        if i%K==0:
            ans+=1
        elif K%2==0 and i%K==K//2:
            ans+=1
    print(ans**3)

if __name__ == '__main__':
    solve()