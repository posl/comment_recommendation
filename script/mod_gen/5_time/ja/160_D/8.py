def solve():
    N,X,Y = map(int,input().split())
    X -= 1
    Y -= 1
    ans = [0]*(N-1)
    for i in range(N):
        for j in range(i+1,N):
            d = min(j-i,abs(X-i)+1+abs(Y-j))
            ans[d-1] += 1
    return ans

if __name__ == '__main__':
    solve()