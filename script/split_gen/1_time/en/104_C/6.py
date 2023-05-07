def main():
    D, G = map(int, input().split())
    p = [0] * (D + 1)
    c = [0] * (D + 1)
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    ans = 10 ** 9
    for i in range(2 ** D):
        s = 0
        cnt = 0
        rest_max = -1
        for j in range(D):
            if (i >> j) & 1:
                s += 100 * (j + 1) * p[j] + c[j]
                cnt += p[j]
            else:
                rest_max = j
        if s < G:
            s1 = 100 * (rest_max + 1)
            need = (G - s + s1 - 1) // s1
            if need >= p[rest_max]:
                continue
            cnt += need
        ans = min(ans, cnt)
    print(ans)
