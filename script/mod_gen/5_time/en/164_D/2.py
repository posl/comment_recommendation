def solve(S):
    N = len(S)
    ans = 0
    for i in range(N):
        for j in range(i, N):
            if int(S[i:j+1]) % 2019 == 0:
                ans += 1
    return ans

if __name__ == '__main__':
    solve()