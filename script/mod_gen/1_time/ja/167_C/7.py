def main():
    N, M, X = map(int, input().split())
    book = [list(map(int, input().split())) for i in range(N)]
    ans = 10 ** 9 + 1
    for i in range(2 ** N):
        cost = 0
        ability = [0] * M
        for j in range(N):
            if (i >> j) & 1:
                cost += book[j][0]
                for k in range(M):
                    ability[k] += book[j][k + 1]
        if min(ability) >= X:
            ans = min(ans, cost)
    if ans == 10 ** 9 + 1:
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    main()