def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S_dic = {}
    for i in range(N):
        if S[i] in S_dic:
            S_dic[S[i]] += 1
            print(S[i] + "(" + str(S_dic[S[i]]) + ")")
        else:
            S_dic[S[i]] = 0
            print(S[i])

if __name__ == '__main__':
    main()