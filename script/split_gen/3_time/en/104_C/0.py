def main():
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    ans = 10**9
    for i in range(2**D):
        score = 0
        count = 0
        for j in range(D):
            if (i >> j) & 1:
                score += 100 * (j + 1) * p[j] + c[j]
                count += p[j]
        if score >= G:
            ans = min(ans, count)
        else:
            for j in range(D - 1, -1, -1):
                if (i >> j) & 1 == 0:
                    for k in range(p[j] - 1):
                        score += 100 * (j + 1)
                        count += 1
                        if score >= G:
                            ans = min(ans, count)
                    break
    print(ans)
