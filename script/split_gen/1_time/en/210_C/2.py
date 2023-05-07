def main():
    N, K = map(int, input().split())
    C = list(map(int, input().split()))
    D = {}
    for i in range(K):
        D[C[i]] = D.get(C[i], 0) + 1
    ans = len(D)
    for i in range(N-K):
        D[C[i]] -= 1
        if D[C[i]] == 0:
            del D[C[i]]
        D[C[i+K]] = D.get(C[i+K], 0) + 1
        ans = max(ans, len(D))
    print(ans)
