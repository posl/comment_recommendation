def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    d = {}
    for i in range(N):
        if S[i] in d:
            d[S[i]] += 1
        else:
            d[S[i]] = 1
        if d[S[i]] == 1:
            print(S[i])
        else:
            print(S[i]+'('+str(d[S[i]])+')')
    return
