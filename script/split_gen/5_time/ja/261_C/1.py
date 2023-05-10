def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    #print(S)
    d = {}
    for i in range(N):
        if S[i] in d:
            d[S[i]] += 1
            print(S[i]+'('+str(d[S[i]])+')')
        else:
            d[S[i]] = 0
            print(S[i])
