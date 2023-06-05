def main():
    D, G = map(int,input().split())
    p = []
    c = []
    for i in range(D):
        pi, ci = map(int,input().split())
        p.append(pi)
        c.append(ci)
    ans = 100000000000000000000
    for i in range(2**D):
        count = 0
        score = 0
        rest_max = -1
        for j in range(D):
            if ((i >> j) & 1):
                score += 100 * (j+1) * p[j] + c[j]
                count += p[j]
            else:
                rest_max = j
        if score < G:
            s1 = 100 * (rest_max+1)
            need = (G - score + s1 - 1) // s1
            if need >= p[rest_max]:
                continue
            count += need
        ans = min(ans,count)
    print(ans)
