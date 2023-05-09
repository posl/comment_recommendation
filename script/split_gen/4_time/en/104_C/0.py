def main():
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    ans = 100000000000000
    for i in range(2 ** D):
        score = 0
        num = 0
        for j in range(D):
            if (i >> j) & 1:
                score += 100 * (j + 1) * p[j] + c[j]
                num += p[j]
        if score >= G:
            ans = min(ans, num)
            continue
        for j in range(D - 1, -1, -1):
            if (i >> j) & 1:
                continue
            for k in range(p[j]):
                score += 100 * (j + 1)
                num += 1
                if score >= G:
                    ans = min(ans, num)
                    break
            break
    print(ans)
