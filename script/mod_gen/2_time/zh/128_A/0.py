def solve(n, m, a, b, c):
    bc = []
    for i in range(m):
        bc.append((b[i], c[i]))
    bc.sort(key=lambda x: x[1], reverse=True)
    # print(bc)
    i = 0
    ans = 0
    for k in range(n):
        if i < m and bc[i][0] > 0:
            ans += bc[i][1]
            bc[i] = (bc[i][0] - 1, bc[i][1])
        else:
            ans += a[k]
        # print(ans)
        while i < m and bc[i][0] == 0:
            i += 1
    return ans

if __name__ == '__main__':
    solve()