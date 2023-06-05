def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    for i in range(N):
        if S[i] not in S[:i]:
            print(S[i])
        else:
            j = S[:i].count(S[i])
            print(S[i] + "(" + str(j+1) + ")")
