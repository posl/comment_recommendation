def main():
    D, G = map(int, input().split())
    p = []
    c = []
    for i in range(D):
        p_i, c_i = map(int, input().split())
        p.append(p_i)
        c.append(c_i)
    ans = 10000000000000000000
    for i in range(2 ** D):
        sum = 0
        cnt = 0
        rest_max = -1
        for j in range(D):
            if (i >> j) & 1:
                sum += 100 * (j + 1) * p[j] + c[j]
                cnt += p[j]
            else:
                rest_max = j
        if sum < G:
            s1 = 100 * (rest_max + 1)
            need = (G - sum + s1 - 1) // s1
            if need >= p[rest_max]:
                continue
            cnt += need
        ans = min(ans, cnt)
    print(ans)
