def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    S = sorted(P[:K])
    print(S[K-1])
    for i in range(K, N):
        S.append(P[i])
        S.sort()
        print(S[K-1])
