def solve(N, C):
    ans = 1
    C.sort()
    for i, c in enumerate(C):
        ans *= max(0, c - i)
        ans %= 10**9 + 7
    return ans
N = int(input())
C = list(map(int, input().split()))
print(solve(N, C))

if __name__ == '__main__':
    solve()