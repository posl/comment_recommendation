def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    P = [p-1 for p in P]
    res = -10**18
    for i in range(N):
        now = i
        score = 0
        loop = []
        while True:
            now = P[now]
            score += C[now]
            loop.append(score)
            if now == i:
                break
        looplen = len(loop)
        if score <= 0:
            res = max(res, max(loop))
        else:
            res = max(res, max(loop) + (K//looplen)*score)
            res = max(res, max(loop[:K%looplen]) + (K//looplen)*score)
    print(res)

if __name__ == '__main__':
    main()