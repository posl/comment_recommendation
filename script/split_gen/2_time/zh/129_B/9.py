def solve():
    N = int(input())
    W = list(map(int,input().split()))
    ans = 10000000
    for i in range(1,N):
        s1 = sum(W[:i])
        s2 = sum(W[i:])
        ans = min(ans,abs(s1-s2))
    print(ans)
