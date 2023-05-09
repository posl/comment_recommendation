def main():
    N = int(input())
    S = [input() for _ in range(N)]
    dic = {}
    for i in range(N):
        if S[i] not in dic:
            dic[S[i]] = 1
            print(S[i])
        else:
            dic[S[i]] += 1
            print(S[i]+"("+str(dic[S[i]]-1)+")")
