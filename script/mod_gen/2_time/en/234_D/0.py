def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    S = sorted(P[:K])
    print(S[K - 1])
    for i in range(K, N):
        S.remove(P[i - K])
        S.insert(bisect.bisect_left(S, P[i]), P[i])
        print(S[K - 1])

if __name__ == '__main__':
    main()