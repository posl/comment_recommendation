def main():
    d, g = map(int, input().split())
    p = []
    c = []
    for i in range(d):
        a, b = map(int, input().split())
        p.append(a)
        c.append(b)
    ans = 10 ** 10
    for i in range(1 << d):
        count = 0
        score = 0
        rest_max = -1
        for j in range(d):
            if (i >> j) & 1:
                score += 100 * (j + 1) * p[j] + c[j]
                count += p[j]
            else:
                rest_max = j
        if score < g:
            s1 = 100 * (rest_max + 1)
            need = (g - score + s1 - 1) // s1
            if need >= p[rest_max]:
                continue
            count += need
        ans = min(ans, count)
    print(ans)
