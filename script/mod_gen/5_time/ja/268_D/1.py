def main():
    N, M = map(int, input().split())
    S = [input() for i in range(N)]
    T = [input() for i in range(M)]
    if N == 1 and M == 1:
        if S[0] == T[0]:
            print(-1)
        else:
            print(S[0])
    else:
        ans = -1
        for i in range(N):
            for j in range(M):
                if S[i] == T[j]:
                    continue
                else:
                    ans = S[i]
                    break
            if ans != -1:
                break
        print(ans)

if __name__ == '__main__':
    main()