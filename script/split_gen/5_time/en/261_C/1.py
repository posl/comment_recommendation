def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    for i in range(N):
        if S.count(S[i]) == 1:
            print(S[i])
        else:
            print(S[i]+'('+str(S[:i].count(S[i]))+')')
