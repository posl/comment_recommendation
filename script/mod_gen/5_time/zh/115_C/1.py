def solve():
    n,k = map(int,input().split())
    h = [int(input()) for _ in range(n)]
    h = sorted(h)
    ans = 10**9
    for i in range(n-k+1):
        ans = min(ans,h[i+k-1]-h[i])
    print(ans)

if __name__ == '__main__':
    solve()