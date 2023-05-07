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
    if N1 > N2 + N3:
        print("UNSOLVABLE")
        return
    if N1 == N3 and S1[-1] == S3[-1]:
        print("UNSOLVABLE")
        return
    if N1 == N3 and S1[-1] != S3[-1]:
        print("UNSOLVABLE")
        return
    if N1 == N2 + N3 and S1[-1] != S3[-1]:
        print("UNSOLVABLE")
        return
    for i in range(10):
        for j in range(10):
            for k in range(10):
                if i == j or j == k or k == i:
                    continue
                if S1[-1] == S3[-1] and S1[-1] == S2[-1]:
                    if S1[-2] == S2[-2]:
                        if int(S1[-1]) + int(S2[-1]) + int(S1[-2]) != int(S3[-1]) + int(S1[-2]) * 10:
                            continue
                    else:
                        if int(S1[-1]) + int(S2[-1]) != int(S3[-1]):
                            continue
                elif S1[-1] == S3[-1]:
                    if S1[-2] == S2[-2]:
                        if int(S1[-1]) + int(S2[-1]) + int(S1[-2]) != int(S3[-1]) + int(S1[-2]) * 10:
                            continue
                    else:
                        if int(S1[-1]) + int(S2[-1]) != int

if __name__ == '__main__':
    main()