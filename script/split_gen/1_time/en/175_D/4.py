def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = -10**9
    for i in range(N):
        x = i
        score = 0
        path = []
        while True:
            x = P[x] - 1
            score += C[x]
            path.append(x)
            if x == i:
                break
        if score <= 0:
            ans = max(ans, max(C))
        else:
            cycle = len(path)
            loop = min(K // cycle, 2 * 10**5)
            score = score * loop
            ans = max(ans, score)
            for j in range(loop * cycle, K):
                x = P[x] - 1
                score += C[x]
                ans = max(ans, score)
    print(ans)
