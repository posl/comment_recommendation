def main():
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    ans = 10**9
    for bit in range(1<<D):
        score = 0
        cnt = 0
        for i in range(D):
            if bit & (1<<i):
                score += 100 * (i+1) * p[i] + c[i]
                cnt += p[i]
        if score < G:
            for i in range(D-1, -1, -1):
                if bit & (1<<i):
                    continue
                for j in range(p[i]):
                    if score >= G:
                        break
                    score += 100 * (i+1)
                    cnt += 1
                break
        if score >= G:
            ans = min(ans, cnt)
    print(ans)

if __name__ == '__main__':
    main()