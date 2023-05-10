def solve(N, D, LRs):
    LRs.sort()
    ans = 1
    for i in range(N-1):
        if LRs[i+1][0] - LRs[i][1] >= D:
            ans += 1
    return ans
N, D = map(int, input().split())
LRs = [list(map(int, input().split())) for _ in range(N)]
print(solve(N, D, LRs))

if __name__ == '__main__':
    solve()