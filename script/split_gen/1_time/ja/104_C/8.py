def main():
    D, G = map(int, input().split())
    p = []
    c = []
    for i in range(D):
        p.append(list(map(int, input().split())))
    for i in range(D):
        c.append(p[i][1] + p[i][0] * 100)
    cnt = 0
    for i in range(D):
        cnt += p[i][0]
    for i in range(D):
        if G < c[i]:
            for j in range(p[i][0]):
                if G < (j + 1) * 100 * (i + 1):
                    cnt = min(cnt, j + 1)
                    break
            break
        else:
            G -= c[i]
    if G > 0:
        cnt = min(cnt, cnt - G // (100 * (i + 1)))
    print(cnt)
