def solve():
    S1 = input()
    S2 = input()
    S3 = input()
    S = S1 + S2 + S3
    S = list(S)
    S = list(set(S))
    if len(S) > 10:
        print("UNSOLVABLE")
        return
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    for m in range(10):
                        for n in range(10):
                            for o in range(10):
                                for p in range(10):
                                    for q in range(10):
                                        for r in range(10):
                                            if i == 0 and S[0] == S1[0]:
                                                continue
                                            if j == 0 and S[1] == S1[0]:
                                                continue
                                            if k == 0 and S[2] == S1[0]:
                                                continue
                                            if l == 0 and S[3] == S1[0]:
                                                continue
                                            if m == 0 and S[4] == S2[0]:
                                                continue
                                            if n == 0 and S[5] == S2[0]:
                                                continue
                                            if o == 0 and S[6] == S2[0]:
                                                continue
                                            if p == 0 and S[7] == S2[0]:
                                                continue
                                            if q == 0 and S[8] == S3[0]:
                                                continue
                                            if r == 0 and S[9] == S3[0]:
                                                continue
                                            if S[0] == S1[0]:
                                                N1 = i*1000 + j*100 + k*10 + l
                                            elif S[0] == S2[0]:
                                                N1 = m*1000 + n*100 + o*10 + p
                                            else:
                                                N1 = q*1000 + r*100 + i*10 + j
                                            if S[1] == S1[0]:
                                                N2 = i*1000 + j*100 + k*10 + l
                                            elif S[1] == S2[0]:
                                                N2 = m*1000 + n*100 + o*10 + p
                                            else:
                                                N2 = q*
