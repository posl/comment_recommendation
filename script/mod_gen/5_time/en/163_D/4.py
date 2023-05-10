def solve():
    #import sys
    #input = sys.stdin.readline
    n, k = map(int, input().split())
    mod = 10**9 + 7
    ans = 0
    for i in range(k, n+2):
        ans += (n-i+1)*i + 1
        ans %= mod
    print(ans)
solve()

if __name__ == '__main__':
    solve()