def main():
    D, G = map(int, input().split())
    P = [0] * D
    C = [0] * D
    for i in range(D):
        P[i], C[i] = map(int, input().split())
    ans = 0
    for i in range(2 ** D):
        score = 0
        count = 0
        for j in range(D):
            if (i >> j) & 1:
                score += 100 * (j + 1) * P[j] + C[j]
                count += P[j]
        if score >= G:
            ans = count
            break
        for j in range(D):
            if (i >> j) & 1:
                continue
            for k in range(P[j] - 1):
                if score >= G:
                    break
                score += 100 * (j + 1)
                count += 1
            if score >= G:
                ans = count
                break
        if score >= G:
            break
    print(ans)
