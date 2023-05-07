def main():
    D, G = map(int, input().split())
    P = []
    C = []
    for i in range(D):
        p, c = map(int, input().split())
        P.append(p)
        C.append(c)
    min_count = 10**9
    for i in range(2**D):
        count = 0
        score = 0
        for j in range(D):
            if i >> j & 1:
                count += P[j]
                score += 100 * (j+1) * P[j] + C[j]
        if score >= G:
            min_count = min(min_count, count)
        else:
            for j in range(D-1, -1, -1):
                if not i >> j & 1:
                    for k in range(P[j]):
                        if score >= G:
                            break
                        else:
                            score += 100 * (j+1)
                            count += 1
            min_count = min(min_count, count)
    print(min_count)

if __name__ == '__main__':
    main()