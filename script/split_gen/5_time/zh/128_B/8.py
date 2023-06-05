def main():
    N = int(input())
    S = []
    P = []
    for i in range(N):
        S.append(input().split()[0])
        P.append(int(input().split()[1]))
    for i in range(N):
        for j in range(N-i-1):
            if S[j] > S[j+1]:
                S[j],S[j+1] = S[j+1],S[j]
                P[j],P[j+1] = P[j+1],P[j]
            elif S[j] == S[j+1]:
                if P[j] < P[j+1]:
                    P[j],P[j+1] = P[j+1],P[j]
    for i in range(N):
        print(P[i])
