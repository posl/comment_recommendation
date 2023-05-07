def main():
    N = int(input())
    S = []
    P = []
    for i in range(N):
        s, p = input().split()
        S.append(s)
        P.append(int(p))
    for i in range(N):
        for j in range(N - 1, i, -1):
            if S[j] < S[j - 1]:
                S[j], S[j - 1] = S[j - 1], S[j]
                P[j], P[j - 1] = P[j - 1], P[j]
            elif S[j] == S[j - 1]:
                if P[j] > P[j - 1]:
                    S[j], S[j - 1] = S[j - 1], S[j]
                    P[j], P[j - 1] = P[j - 1], P[j]
    for i in range(N):
        print(i + 1)

if __name__ == '__main__':
    main()