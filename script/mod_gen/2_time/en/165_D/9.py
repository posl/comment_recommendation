def solve():
    A,B,N = map(int,input().split())
    X = min(N,B-1)
    ans = A*X//B - A*(X//B)
    print(ans)
solve()
