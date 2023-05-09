def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = -10 ** 18
    for i in range(N):
        s = []
        j = i
        while True:
            s.append(C[j])
            j = P[j] - 1
            if j == i:
                break
        l = len(s)
        score = 0
        for k in range(l):
            score += s[k]
            if score <= 0:
                continue
            if K < k + 1:
                break
            if l < K:
                ans = max(ans, score * (K // (k + 1)))
            else:
                ans = max(ans, score)
    print(ans)
