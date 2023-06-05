def solve(S):
    ans = 1000000000000000000000000000
    for i in range(len(S)):
        for j in range(i, len(S)):
            if S[i] != '0' or j == i:
                ans = min(ans, i + len(S) - j + S.count('0', i, j+1))
    return ans

if __name__ == '__main__':
    solve()