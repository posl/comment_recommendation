def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S_dict = {}
    for i in range(N):
        if S[i] in S_dict:
            S_dict[S[i]] += 1
            S[i] += '(' + str(S_dict[S[i]]) + ')'
        else:
            S_dict[S[i]] = 0
    for i in range(N):
        print(S[i])
