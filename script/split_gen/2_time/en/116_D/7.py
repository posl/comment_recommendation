def main():
    import sys
    from collections import defaultdict
    from heapq import heappush, heappop
    input = sys.stdin.readline
    N, K = map(int, input().split())
    S = []
    for _ in range(N):
        t, d = map(int, input().split())
        S.append((t, d))
    S.sort(key=lambda x: x[1], reverse=True)
    D = defaultdict(int)
    D[S[0][0]] = 1
    X = [S[0][1]]
    for i in range(1, K):
        D[S[i][0]] += 1
        X.append(S[i][1])
    x = len(D)
    ans = sum(X) + x*x
    for i in range(K, N):
        if D[S[i][0]] > 0:
            D[S[i][0]] += 1
            X.append(S[i][1])
            continue
        D[S[i][0]] += 1
        X.append(S[i][1])
        X.sort()
        x += 1
        ans = max(ans, sum(X[:-1]) + x*x)
    print(ans)
