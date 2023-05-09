def main():
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    ans = 10**9
    for i in range(2**D):
        tmp = 0
        score = 0
        for j in range(D):
            if (i >> j) & 1:
                tmp += p[j]
                score += 100 * (j+1) * p[j] + c[j]
        if score >= G:
            ans = min(ans, tmp)
        else:
            for j in range(D-1, -1, -1):
                if (i >> j) & 1:
                    continue
                for k in range(p[j]):
                    if score >= G:
                        break
                    score += 100 * (j+1)
                    tmp += 1
                break
            if score >= G:
                ans = min(ans, tmp)
    print(ans)
