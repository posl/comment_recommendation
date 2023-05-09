def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S_dict = {}
    for i in range(N):
        if S[i] not in S_dict:
            S_dict[S[i]] = 1
            print(S[i])
        else:
            S_dict[S[i]] += 1
            print(S[i]+"("+str(S_dict[S[i]]-1)+")")
