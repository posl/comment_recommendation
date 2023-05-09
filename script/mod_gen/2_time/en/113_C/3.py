def main():
    N, M = map(int, input().split())
    P = []
    Y = []
    for _ in range(M):
        p, y = map(int, input().split())
        P.append(p)
        Y.append(y)
    ans = solve(N, M, P, Y)
    for i in range(M):
        print(ans[i])

if __name__ == '__main__':
    main()