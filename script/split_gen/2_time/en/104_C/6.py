def main():
    #input
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    #compute
    ans = 10**9
    for i in range(2**D):
        score = 0
        num = 0
        for j in range(D):
            if (i >> j) & 1:
                score += 100 * (j + 1) * p[j] + c[j]
                num += p[j]
        if score < G:
            for j in range(D):
                if not (i >> (D - 1 - j)) & 1:
                    for k in range(p[D - 1 - j]):
                        if score >= G:
                            break
                        score += 100 * (D - j)
                        num += 1
        if score >= G:
            ans = min(ans, num)
    #output
    print(ans)
