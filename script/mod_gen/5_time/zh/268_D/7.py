def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    S.sort()
    T.sort()
    for i in range(N):
        for j in range(N):
            if i != j:
                for k in range(M):
                    if S[i] + T[k] == S[j]:
                        print(-1)
                        return
    for i in range(N):
        for j in range(M):
            if S[i] == T[j]:
                print(-1)
                return
    ans = ""
    for i in range(N):
        ans += S[i]
        for j in range(M):
            ans += T[j]
    print(ans)

if __name__ == '__main__':
    main()