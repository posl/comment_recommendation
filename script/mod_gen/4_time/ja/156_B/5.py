def solve():
    N,K = map(int,input().split())
    ans = 0
    while N > 0:
        N = N // K
        ans += 1
    print(ans)

if __name__ == '__main__':
    solve()