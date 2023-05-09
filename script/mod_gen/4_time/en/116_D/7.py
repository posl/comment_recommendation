def solve():
    N, K = map(int, input().split())
    sushi = [list(map(int, input().split())) for _ in range(N)]
    sushi.sort(key=lambda x: x[1], reverse=True)
    kind = set()
    ans = 0
    s = 0
    for i in range(N):
        s += sushi[i][1]
        kind.add(sushi[i][0])
        if len(kind) == K:
            ans = max(ans, s + K * K)
        elif len(kind) > K:
            for j in range(i - 1, -1, -1):
                if sushi[i][0] == sushi[j][0]:
                    s -= sushi[j][1]
                    kind.remove(sushi[j][0])
                    break
            ans = max(ans, s + len(kind) * len(kind))
    print(ans)

if __name__ == '__main__':
    solve()