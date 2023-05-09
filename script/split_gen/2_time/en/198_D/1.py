def main():
    S1 = input()
    S2 = input()
    S3 = input()
    N1 = len(S1)
    N2 = len(S2)
    N3 = len(S3)
    if N1 > N3 or N2 > N3:
        print('UNSOLVABLE')
        return
    if N1 < N3 and S1[0] == '0':
        print('UNSOLVABLE')
        return
    if N2 < N3 and S2[0] == '0':
        print('UNSOLVABLE')
        return
    L = set(S1) | set(S2) | set(S3)
    if len(L) > 10:
        print('UNSOLVABLE')
        return
    N = len(L)
    for i in range(10**N):
        S = str(i).zfill(N)
        D = dict(zip(L, S))
        if D[S1[0]] == '0' or D[S2[0]] == '0':
            continue
        N1 = int(''.join([D[s] for s in S1]))
        N2 = int(''.join([D[s] for s in S2]))
        N3 = int(''.join([D[s] for s in S3]))
        if N1 + N2 == N3:
            print(N1)
            print(N2)
            print(N3)
            return
    print('UNSOLVABLE')
