def main():
    X = input()
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    for i in range(N):
        for j in range(N-1):
            if S[j] > S[j+1]:
                S[j], S[j+1] = S[j+1], S[j]
            elif S[j] == S[j+1]:
                continue
            else:
                for k in range(len(S[j])):
                    if X.index(S[j][k]) > X.index(S[j+1][k]):
                        S[j], S[j+1] = S[j+1], S[j]
                        break
                    elif X.index(S[j][k]) == X.index(S[j+1][k]):
                        continue
                    else:
                        break
    for i in range(N):
        print(S[i])
