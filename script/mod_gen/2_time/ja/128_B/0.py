def main():
    N = int(input())
    S = []
    P = []
    for i in range(N):
        s, p = input().split()
        S.append(s)
        P.append(int(p))
    for i in range(N):
        for j in range(N):
            if S[i] < S[j]:
                S[i], S[j] = S[j], S[i]
                P[i], P[j] = P[j], P[i]
            elif S[i] == S[j]:
                if P[i] > P[j]:
                    S[i], S[j] = S[j], S[i]
                    P[i], P[j] = P[j], P[i]
    for i in range(N):
        for j in range(N):
            if S[i] == S[j]:
                if P[i] == P[j]:
                    if i < j:
                        S[i], S[j] = S[j], S[i]
                        P[i], P[j] = P[j], P[i]
    for i in range(N):
        print(S.index(S[i])+1)
main()
