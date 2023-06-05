def main():
    S1 = input()
    S2 = input()
    S3 = input()
    S = set(S1 + S2 + S3)
    if len(S) > 10:
        print("UNSOLVABLE")
        return
    for S in permutations(S):
        if S[0] == '0' or S[3] == '0' or S[6] == '0':
            continue
        D = dict(zip(S, range(10)))
        N1 = sum(D[c] * 10 ** i for i, c in enumerate(S1[::-1]))
        N2 = sum(D[c] * 10 ** i for i, c in enumerate(S2[::-1]))
        N3 = sum(D[c] * 10 ** i for i, c in enumerate(S3[::-1]))
        if N1 + N2 == N3:
            print(N1)
            print(N2)
            print(N3)
            return
    print("UNSOLVABLE")
