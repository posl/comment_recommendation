def main():
    N, K = map(int, input().split())
    TD = [list(map(int, input().split())) for i in range(N)]
    TD.sort(key=lambda x: x[1], reverse=True)
    ans = 0
    kinds = set()
    total = 0
    for i in range(K):
        kinds.add(TD[i][0])
        total += TD[i][1]
    ans = total + len(kinds) ** 2
    for i in range(K, N):
        if len(kinds) == K:
            break
        if TD[i][0] not in kinds:
            kinds.add(TD[i][0])
            total += TD[i][1]
            for j in range(i - 1, -1, -1):
                if TD[j][0] not in kinds:
                    kinds.add(TD[j][0])
                    total -= TD[j][1]
                    ans = max(ans, total + len(kinds) ** 2)
                    break
    print(ans)

if __name__ == '__main__':
    main()