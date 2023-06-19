def main():
    N, M, Q = map(int, input().split())
    query = []
    for i in range(Q):
        a, b, c, d = map(int, input().split())
        query.append((a, b, c, d))
    ans = 0
    for A in range(1, M+1):
        for B in range(A, M+1):
            for C in range(B, M+1):
                for D in range(C, M+1):
                    for E in range(D, M+1):
                        for F in range(E, M+1):
                            for G in range(F, M+1):
                                for H in range(G, M+1):
                                    for I in range(H, M+1):
                                        for J in range(I, M+1):
                                            score = 0
                                            for a, b, c, d in query:
                                                if A <= a and b <= B:
                                                    score += c
                                                if C <= a and b <= D:
                                                    score += c
                                                if E <= a and b <= F:
                                                    score += c
                                                if G <= a and b <= H:
                                                    score += c
                                                if I <= a and b <= J:
                                                    score += c
                                            ans = max(ans, score)
    print(ans)
main()
