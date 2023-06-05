def problems126_a():
    N, K = map(int, input().split())
    S = input()
    S1 = S[K-1]
    S2 = S1.lower()
    S3 = S[:K-1] + S2 + S[K:]
    print(S3)
