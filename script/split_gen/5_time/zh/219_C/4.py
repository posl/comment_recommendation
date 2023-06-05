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
    for i in range(26):
        X_dict[X[i]] = chr(ord('a') + i)
    #print(X_dict)
    S_dict = {}
    for i in range(N):
        S_dict[S[i]] = ''
        for j in range(len(S[i])):
            S_dict[S[i]] += X_dict[S[i][j]]
    #print(S_dict)
    S_dict_sorted = sorted(S_dict.items(), key=lambda x:x[1])
    #print(S_dict_sorted)
    for i in range(N):
        print(S_dict_sorted[i][0])
