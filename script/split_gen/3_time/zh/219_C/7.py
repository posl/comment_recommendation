def main():
    X = input()
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    #print(X)
    #print(N)
    #print(S)
    X_dict = {}
    for i in range(len(X)):
        X_dict[X[i]] = chr(97+i)
    #print(X_dict)
    for i in range(N):
        for j in range(len(S[i])):
            S[i] = S[i].replace(S[i][j], X_dict[S[i][j]])
    #print(S)
    S.sort()
    #print(S)
    for i in range(N):
        for j in range(len(S[i])):
            S[i] = S[i].replace(S[i][j], X[X_dict[S[i][j]]])
    #print(S)
    for i in range(N):
        print(S[i])
