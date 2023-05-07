def solve():
    n = int(input())
    c = list(map(int, input().split()))
    c.sort()
    mod = 1000000007
    ans = 1
    for i in range(n):
        ans *= c[i] - i
        ans %= mod
    print(ans)

if __name__ == '__main__':
    solve()