def main():
    D, G = map(int, input().split())
    p = []
    c = []
    for _ in range(D):
        p_i, c_i = map(int, input().split())
        p.append(p_i)
        c.append(c_i)
    min_num = 1000000
    for i in range(2**D):
        score = 0
        num = 0
        for j in range(D):
            if (i >> j) & 1:
                score += 100 * (j+1) * p[j] + c[j]
                num += p[j]
        if score >= G:
            min_num = min(min_num, num)
        else:
            for j in range(D-1, -1, -1):
                if (i >> j) & 1:
                    continue
                for k in range(p[j]):
                    if score >= G:
                        break
                    score += 100 * (j + 1)
                    num += 1
            min_num = min(min_num, num)
    print(min_num)
