def main():
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    ans = 10**9
    for i in range(1 << D):
        score = 0
        cnt = 0
        for j in range(D):
            if i & (1 << j):
                score += 100 * (j+1) * p[j] + c[j]
                cnt += p[j]
        if score < G:
            for j in range(D-1, -1, -1):
                if not(i & (1 << j)):
                    for k in range(p[j]):
                        if score >= G:
                            break
                        score += 100 * (j+1)
                        cnt += 1
                    break
        if score >= G:
            ans = min(ans, cnt)
    print(ans)
