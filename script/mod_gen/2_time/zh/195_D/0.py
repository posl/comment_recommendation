def solve(n, m, q, w, v, x, l, r):
    ans = 0
    for i in range(1, 2**n):
        if bin(i).count('1') != m:
            continue
        weight = 0
        value = 0
        for j in range(n):
            if i & (1 << j):
                weight += w[j]
                value += v[j]
        for j in range(m):
            if x[j] >= weight and l <= j+1 and j+1 <= r:
                ans = max(ans, value)
    return ans

if __name__ == '__main__':
    solve()