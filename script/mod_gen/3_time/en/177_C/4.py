def solve():
    N = int(input())
    A = [int(a) for a in input().split()]
    s = sum(A)
    ans = 0
    for a in A:
        s -= a
        ans += a * s
        ans %= 1000000007
    print(ans)
solve()

if __name__ == '__main__':
    solve()