def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    ans = ''
    for i in range(N):
        ans += S[i]
        ans += '_'
    ans = ans[:-1]
    for t in T:
        if t in ans:
            print(-1)
            return
    print(ans)

if __name__ == '__main__':
    main()