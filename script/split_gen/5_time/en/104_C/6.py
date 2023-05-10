def main():
    d, g = map(int, input().split())
    p = []
    c = []
    for i in range(d):
        p_i, c_i = map(int, input().split())
        p.append(p_i)
        c.append(c_i)
    ans = 10 ** 9
    for i in range(2 ** d):
        score = 0
        cnt = 0
        rest_max = -1
        for j in range(d):
            if (i >> j) & 1:
                score += 100 * (j + 1) * p[j] + c[j]
                cnt += p[j]
            else:
                rest_max = j
        if score < g:
            s1 = 100 * (rest_max + 1)
            need = (g - score + s1 - 1) // s1
            if need >= p[rest_max]:
                continue
            cnt += need
        ans = min(ans, cnt)
    print(ans)
