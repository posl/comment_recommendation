def main():
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    ans = float("inf")
    for i in range(2 ** D):
        total = 0
        cnt = 0
        for j in range(D):
            if (i >> j) & 1:
                total += 100 * (j + 1) * p[j] + c[j]
                cnt += p[j]
        if total < G:
            for j in range(D - 1, -1, -1):
                if not ((i >> j) & 1):
                    for k in range(p[j]):
                        if total >= G:
                            break
                        total += 100 * (j + 1)
                        cnt += 1
                    break
        if total >= G:
            ans = min(ans, cnt)
    print(ans)
