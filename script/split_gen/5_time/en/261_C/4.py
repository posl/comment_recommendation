def main():
    N = int(input())
    S = [input() for _ in range(N)]
    D = {}
    for i in range(N):
        if S[i] in D:
            D[S[i]] += 1
        else:
            D[S[i]] = 1
        if D[S[i]] == 1:
            print(S[i])
        else:
            print(S[i] + '(' + str(D[S[i]] - 1) + ')')
    return
