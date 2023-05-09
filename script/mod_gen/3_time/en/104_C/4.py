def main():
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    # 2^D通りの解法を全探索
    ans = 10**9
    for bit in range(1 << D):
        score = 0
        num = 0
        for i in range(D):
            if bit & (1 << i):
                # 問題を解く
                score += 100 * (i + 1) * p[i] + c[i]
                num += p[i]
        if score < G:
            # 解いた問題の中で1番難しいものを解く
            for i in range(D - 1, -1, -1):
                if bit & (1 << i):
                    continue
                for j in range(p[i]):
                    score += 100 * (i + 1)
                    num += 1
                    if score >= G:
                        break
                if score >= G:
                    break
        if score >= G:
            ans = min(ans, num)
    print(ans)

if __name__ == '__main__':
    main()