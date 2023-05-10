def solve():
    D, G = map(int, input().split())
    p = []
    c = []
    for _ in range(D):
        p_i, c_i = map(int, input().split())
        p.append(p_i)
        c.append(c_i)
    ans = 1e9
    for mask in range(1 << D):
        score = 0
        num = 0
        rest_max = -1
        for i in range(D):
            if (mask >> i) & 1:
                score += 100 * (i + 1) * p[i] + c[i]
                num += p[i]
            else:
                rest_max = i
        if score < G:
            s1 = 100 * (rest_max + 1)
            need = (G - score + s1 - 1) // s1
            if need >= p[rest_max]:
                continue
            num += need
        ans = min(ans, num)
    print(ans)

if __name__ == '__main__':
    solve()