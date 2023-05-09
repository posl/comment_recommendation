def solve(N, K, P):
    S = []
    for i in range(N):
        if len(S) == 0:
            S.append(P[i])
        else:
            if P[i] > S[-1]:
                S.append(P[i])
            else:
                l = 0
                r = len(S) - 1
                while r - l > 1:
                    m = (l + r) // 2
                    if S[m] >= P[i]:
                        r = m
                    else:
                        l = m
                S[r] = P[i]
    return S
