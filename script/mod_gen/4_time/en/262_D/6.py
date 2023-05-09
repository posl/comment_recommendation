def solve():
    N = int(input())
    A = [int(x) for x in input().split()]
    A.sort()
    A.reverse()
    mod = 998244353
    ans = 0
    for i in range(1,N+1):
        ans = (ans + (A[i-1] * (2**(i-1)) * (2**(N-i))))%mod
    print(ans)
solve()

if __name__ == '__main__':
    solve()