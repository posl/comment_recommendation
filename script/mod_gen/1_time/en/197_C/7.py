def solve():
    N=int(input())
    A=list(map(int,input().split()))
    ans=0
    for i in range(30):
        B=[a>>i&1 for a in A]
        if B.count(1)%2==1:
            ans+=1<<i
    print(ans)

if __name__ == '__main__':
    solve()