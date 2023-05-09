def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    S = sorted(P[:K])
    for i in range(N - K):
        print(S[K - 1])
        S.remove(P[i])
        S.insert(bisect.bisect_left(S, P[i + K]), P[i + K])
    print(S[K - 1])
