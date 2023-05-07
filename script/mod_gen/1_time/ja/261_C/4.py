def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    ans = []
    for i in range(N):
        if S[i] not in S[:i]:
            ans.append(S[i])
        else:
            X = S[:i].count(S[i])
            ans.append(S[i] + "(" + str(X) + ")")
    for i in range(N):
        print(ans[i])

if __name__ == '__main__':
    main()