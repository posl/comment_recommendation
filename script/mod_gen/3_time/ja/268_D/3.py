def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    ans = ''
    for i in range(N):
        ans += S[i] + '_'
    ans = ans[:-1]
    if ans in T:
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    main()