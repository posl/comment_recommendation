def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    D = {}
    for i in range(N):
        if S[i] in D:
            D[S[i]] += 1
            print(S[i] + "(" + str(D[S[i]]) + ")")
        else:
            D[S[i]] = 0
            print(S[i])
