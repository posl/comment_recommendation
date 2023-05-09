def main():
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    ans = 10**9
    for bit in range(2**D):
        cnt = 0
        score = 0
        for i in range(D):
            if bit & (1 << i):
                cnt += p[i]
                score += 100 * (i + 1) * p[i] + c[i]
        if score >= G:
            ans = min(ans, cnt)
        else:
            for i in range(D - 1, -1, -1):
                if bit & (1 << i):
                    continue
                for j in range(p[i]):
                    cnt += 1
                    score += 100 * (i + 1)
                    if score >= G:
                        ans = min(ans, cnt)
                        break
                break
    print(ans)
