def main():
    N,M = map(int,input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    for i in range(N):
        for j in range(M):
            if S[i] == T[j]:
                print(-1)
                return
    for i in range(N):
        for j in range(M):
            if S[i] in T[j]:
                print(-1)
                return
    ans = ''
    for i in range(N):
        ans += S[i]
        if i != N-1:
            ans += '_'
    print(ans)

if __name__ == '__main__':
    main()