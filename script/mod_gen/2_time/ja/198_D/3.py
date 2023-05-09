def solve():
    S1 = input()
    S2 = input()
    S3 = input()
    if len(S1) != len(S2) or len(S2) != len(S3):
        print("UNSOLVABLE")
        exit()
    if len(set(S1)) > 10 or len(set(S2)) > 10 or len(set(S3)) > 10:
        print("UNSOLVABLE")
        exit()
    N1 = []
    N2 = []
    N3 = []
    for i in range(len(S1)):
        N1.append(S1[i])
        N2.append(S2[i])
        N3.append(S3[i])
    N1 = set(N1)
    N2 = set(N2)
    N3 = set(N3)
    if len(N1) > 10 or len(N2) > 10 or len(N3) > 10:
        print("UNSOLVABLE")
        exit()
    if len(N1) + len(N2) + len(N3) > 10:
        print("UNSOLVABLE")
        exit()
    N1 = list(N1)
    N2 = list(N2)
    N3 = list(N3)
    for i in range(10):
        for j in range(10):
            for k in range(10):
                if i in N1 or j in N2 or k in N3:
                    continue
                if len(N1) == 1:
                    if N1[0] == S1[0] and i == 0:
                        continue
                if len(N2) == 1:
                    if N2[0] == S2[0] and j == 0:
                        continue
                if len(N3) == 1:
                    if N3[0] == S3[0] and k == 0:
                        continue
                for l in range(len(S1)):
                    if S1[l] == N1[0]:
                        S1 = S1.replace(S1[l], str(i))
                    if S2[l] == N2[0]:
                        S2 = S2.replace(S2[l], str(j))
                    if S3[l] == N3[0]:
                        S3 = S3.replace(S3[l], str(k))
                if int(S1) + int(S2) == int(S3):

if __name__ == '__main__':
    solve()