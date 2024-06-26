def main():
    # Read input
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    
    # Solve
    ans = 10 ** 9
    for i in range(2 ** D):
        cnt = 0
        score = 0
        for j in range(D):
            if i & (1 << j):
                cnt += p[j]
                score += 100 * (j + 1) * p[j] + c[j]
        if score >= G:
            ans = min(ans, cnt)
        else:
            for j in range(D - 1, -1, -1):
                if not i & (1 << j):
                    for k in range(p[j]):
                        cnt += 1
                        score += 100 * (j + 1)
                        if score >= G:
                            ans = min(ans, cnt)
                        if score >= G:
                            break
                    break
    print(ans)
main()
