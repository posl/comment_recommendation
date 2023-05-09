def solve():
    N,K = map(int,input().split())
    p = list(map(int,input().split()))
    psum = [0]
    for i in range(N):
        psum.append(psum[i]+p[i])
    ans = 0
    for i in range(N-K+1):
        ans = max(ans,(psum[i+K]-psum[i])/2+K/2)
    print(ans)

if __name__ == '__main__':
    solve()