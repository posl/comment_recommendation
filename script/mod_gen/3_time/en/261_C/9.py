def main():
    N = int(input())
    S = [input() for _ in range(N)]
    #print(S)
    D = {}
    for i in range(N):
        if S[i] in D:
            D[S[i]] += 1
            S[i] = S[i] + '(' + str(D[S[i]]) + ')'
        else:
            D[S[i]] = 0
    for i in range(N):
        print(S[i])
main()
