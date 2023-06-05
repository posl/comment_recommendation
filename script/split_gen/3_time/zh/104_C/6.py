def main():
    d, g = map(int, input().split())
    p = []
    c = []
    for i in range(d):
        pi, ci = map(int, input().split())
        p.append(pi)
        c.append(ci)
    ans = 1000
    for i in range(2**d):
        point = 0
        num = 0
        rest_max = -1
        for j in range(d):
            if (i >> j) & 1:
                point += 100 * (j + 1) * p[j] + c[j]
                num += p[j]
            else:
                rest_max = j
        if point < g:
            s1 = 100 * (rest_max + 1)
            need = (g - point + s1 - 1) // s1
            if need >= p[rest_max]:
                continue
            num += need
        ans = min(ans, num)
    print(ans)
