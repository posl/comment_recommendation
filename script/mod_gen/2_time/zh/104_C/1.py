def solve(D, G, P, C):
    ans = float('inf')
    for i in range(1 << D):
        s = 0
        cnt = 0
        rest_max = -1
        for j in range(D):
            if (i >> j) & 1:
                s += P[j] * 100 * (j + 1) + C[j]
                cnt += P[j]
            else:
                rest_max = j
        if s < G:
            s1 = 100 * (rest_max + 1)
            need = (G - s + s1 - 1) // s1
            if need >= P[rest_max]:
                continue
            cnt += need
        ans = min(ans, cnt)
    return ans

if __name__ == '__main__':
    solve()