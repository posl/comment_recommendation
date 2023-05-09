def main():
    d, g = map(int, input().split())
    p = [0] * d
    c = [0] * d
    for i in range(d):
        p[i], c[i] = map(int, input().split())
    ans = 1000000000000000
    for i in range(2 ** d):
        score = 0
        cnt = 0
        for j in range(d):
            if (i >> j) & 1:
                score += (j + 1) * 100 * p[j] + c[j]
                cnt += p[j]
        if score >= g:
            ans = min(ans, cnt)
        else:
            for j in reversed(range(d)):
                if (i >> j) & 1:
                    continue
                for k in range(p[j]):
                    if score >= g:
                        break
                    score += (j + 1) * 100
                    cnt += 1
            ans = min(ans, cnt)
    print(ans)
