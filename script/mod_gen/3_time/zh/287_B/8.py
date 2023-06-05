def main():
    #N, M = map(int, input().split())
    #S = [input() for _ in range(N)]
    #T = [input() for _ in range(M)]
    S = ['000000', '123456', '987111', '000000']
    T = ['000', '111', '999', '111']
    ans = 0
    for i in range(len(S)):
        for j in range(len(T)):
            if S[i][-3:] == T[j]:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()