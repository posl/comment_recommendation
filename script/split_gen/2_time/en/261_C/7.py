def main():
    N = int(input())
    S = [input() for i in range(N)]
    S_dict = {}
    for i in range(N):
        if S[i] in S_dict:
            S_dict[S[i]] += 1
            print(S[i] + "(" + str(S_dict[S[i]]) + ")")
        else:
            S_dict[S[i]] = 0
            print(S[i])
    return 0
