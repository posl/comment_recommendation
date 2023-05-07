def main():
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    #print(p)
    #print(c)
    #print(D, G)
    min_num = 1000
    for i in range(2**D):
        sum_score = 0
        num = 0
        for j in range(D):
            if ((i >> j) & 1):
                sum_score += 100 * (j + 1) * p[j] + c[j]
                num += p[j]
        if sum_score >= G:
            if min_num > num:
                min_num = num
        else:
            for j in range(D):
                if ((i >> j) & 1) == 0:
                    for k in range(p[j]):
                        sum_score += 100 * (j + 1)
                        num += 1
                        if sum_score >= G:
                            if min_num > num:
                                min_num = num
                            break
                    break
    print(min_num)
