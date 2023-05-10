def main():
    N = int(input())
    S = []
    P = []
    for i in range(N):
        s, p = input().split()
        S.append(s)
        P.append(int(p))
    #print(S)
    #print(P)
    dic = {}
    for i in range(N):
        if S[i] in dic:
            dic[S[i]].append([P[i], i+1])
        else:
            dic[S[i]] = [[P[i], i+1]]
    #print(dic)
    for i in dic:
        dic[i].sort(reverse=True)
    #print(dic)
    S.sort()
    #print(S)
    for i in S:
        for j in range(len(dic[i])):
            print(dic[i][j][1])
