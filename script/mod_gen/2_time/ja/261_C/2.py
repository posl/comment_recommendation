def main():
    N = int(input())
    S = [input() for _ in range(N)]
    ans = []
    for i in range(N):
        if S[i] in S[:i]:
            ans.append(S[i] + "(" + str(S[:i].count(S[i])) + ")")
        else:
            ans.append(S[i])
    for i in range(N):
        print(ans[i])

if __name__ == '__main__':
    main()