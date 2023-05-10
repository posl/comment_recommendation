def solve(N, A):
    cnt = [0] * 200
    for a in A:
        cnt[a % 200] += 1
    ans = 0
    for c in cnt:
        ans += c * (c - 1) // 2
    return ans

if __name__ == '__main__':
    solve()