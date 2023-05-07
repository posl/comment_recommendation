def dfs(a, i, n, m, q, abcd):
    if i == n:
        score = 0
        for j in range(q):
            if a[abcd[j][1] - 1] - a[abcd[j][0] - 1] == abcd[j][2]:
                score += abcd[j][3]
        return score
    ans = 0
    for j in range(a[i - 1], m + 1):
        a[i] = j
        ans = max(ans, dfs(a, i + 1, n, m, q, abcd))
    return ans

if __name__ == '__main__':
    dfs()