def main():
    N = int(input())
    S = [input() for i in range(N)]
    ans = []
    for i in range(N):
        if S[i] in ans:
            cnt = 0
            for j in range(i):
                if S[i] == S[j]:
                    cnt += 1
            ans.append(S[i] + "(" + str(cnt) + ")")
        else:
            ans.append(S[i])
    for i in range(N):
        print(ans[i])

if __name__ == '__main__':
    main()