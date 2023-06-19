def solve(n, a, q, query):
    ans = []
    for l, r, x in query:
        ans.append(a[l - 1:r].count(x))
    return ans

if __name__ == '__main__':
    solve()