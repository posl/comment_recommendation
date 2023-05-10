def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    # print(N,M)
    # print(S)
    # print(T)
    # print(S[0][-3:])
    # print(T[0])
    # print(S[0][-3:] == T[0])
    ans = 0
    for s in S:
        for t in T:
            if s[-3:] == t:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()