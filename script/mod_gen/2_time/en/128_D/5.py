def solve():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for left in range(min(N, K) + 1):
        for right in range(min(N, K) - left + 1):
            if left + right > N:
                continue
            tmp = V[:left] + V[N - right:]
            tmp.sort()
            ans = max(ans, sum(tmp[-K:]))
    return ans
print(solve())
import sys

if __name__ == '__main__':
    solve()