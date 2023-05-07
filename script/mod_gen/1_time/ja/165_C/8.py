def dfs(a, n, m, q, a_i, b_i, c_i, d_i):
    if len(a) == n:
        return score(a, q, a_i, b_i, c_i, d_i)
    if len(a) == 0:
        num = 1
    else:
        num = a[-1]
    ans = 0
    while num <= m:
        a.append(num)
        ans = max(ans, dfs(a, n, m, q, a_i, b_i, c_i, d_i))
        a.pop()
        num += 1
    return ans

if __name__ == '__main__':
    dfs()