def solve():
    S1 = input()
    S2 = input()
    S3 = input()
    N1 = len(S1)
    N2 = len(S2)
    N3 = len(S3)
    if N1 < N3 or N2 < N3:
        print("UNSOLVABLE")
        return
    if N1 > N3:
        if S1[0] == '0':
            print("UNSOLVABLE")
            return
    if N2 > N3:
        if S2[0] == '0':
            print("UNSOLVABLE")
            return
    if N1 == N3:
        if S1[0] == '0':
            print("UNSOLVABLE")
            return
    if N2 == N3:
        if S2[0] == '0':
            print("UNSOLVABLE")
            return
    if S3[0] == '0':
        if N1 == N3 and N2 == N3:
            print("UNSOLVABLE")
            return
        if N1 == N3:
            if S2[0] == '0':
                print("UNSOLVABLE")
                return
        if N2 == N3:
            if S1[0] == '0':
                print("UNSOLVABLE")
                return
    if N1 > N2:
        print("UNSOLVABLE")
        return
    if N1 == N2:
        if S1[0] < S2[0]:
            print("UNSOLVABLE")
            return
    S = S1 + S2 + S3
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
                                            if len(set([i, j, k, l, m, n, o, p, q, r])) == 10:
                                                S1_ = S1.replace(S[0], str(i)).replace

if __name__ == '__main__':
    solve()