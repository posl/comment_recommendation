def main():
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    ans = 10000
    for i in range(2 ** D):
        score = 0
        cnt = 0
        for j in range(D):
            if i & (1 << j):
                score += 100 * (j + 1) * p[j] + c[j]
                cnt += p[j]
        if score < G:
            for j in range(D - 1, -1, -1):
                if not (i & (1 << j)):
                    for k in range(p[j]):
                        score += 100 * (j + 1)
                        cnt += 1
                        if score >= G:
                            ans = min(ans, cnt)
                            break
                    break
        else:
            ans = min(ans, cnt)
    print(ans)

if __name__ == '__main__':
    main()