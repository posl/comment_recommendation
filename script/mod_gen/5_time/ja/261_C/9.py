def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S_dict = {}
    for i in range(N):
        if S[i] in S_dict:
            S_dict[S[i]] += 1
        else:
            S_dict[S[i]] = 1
        if S_dict[S[i]] == 1:
            print(S[i])
        else:
            print(S[i] + "(" + str(S_dict[S[i]]-1) + ")")

if __name__ == '__main__':
    main()