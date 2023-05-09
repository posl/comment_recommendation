def main():
    S1 = input()
    S2 = input()
    S3 = input()
    N1 = len(S1)
    N2 = len(S2)
    N3 = len(S3)
    if N1 < N2:
        S1, S2 = S2, S1
        N1, N2 = N2, N1
    if N1 < N3:
        S1, S3 = S3, S1
        N1, N3 = N3, N1
    if N2 < N3:
        S2, S3 = S3, S2
        N2, N3 = N3, N2
    D = {}
    for i in range(N1):
        D[S1[i]] = 0
    for i in range(N2):
        D[S2[i]] = 0
    for i in range(N3):
        D[S3[i]] = 0
    #print(D)
    #print(N1, N2, N3)
    if N1 == N3:
        for i in range(10):
            if S1[0] == S3[0] and i == 0:
                continue
            if S2[0] == S3[0] and i == 0:
                continue
            D[S1[0]] = i
            for j in range(10):
                if S1[1] == S3[1] and j == 0:
                    continue
                if S2[1] == S3[1] and j == 0:
                    continue
                D[S2[0]] = j
                for k in range(10):
                    if S1[2] == S3[2] and k == 0:
                        continue
                    if S2[2] == S3[2] and k == 0:
                        continue
                    D[S3[0]] = k
                    #print(D)
                    if D[S1[0]] + D[S2[0]] == D[S3[0]]:
                        if D[S1[1]] + D[S2[1]] == D[S3[1]]:
                            if D[S1[2]] + D[S2[2]] == D[S3[2]]:
                                print(D[S1[0]]*100+D[S1

if __name__ == '__main__':
    main()