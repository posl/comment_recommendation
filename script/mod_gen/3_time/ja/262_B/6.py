def main():
    #入力
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    #グラフを作成
    G = [[] for _ in range(N)]
    for a, b in AB:
        a -= 1
        b -= 1
        G[a].append(b)
        G[b].append(a)
    #グラフを探索
    ans = 0
    for a in range(N):
        for b in G[a]:
            if a >= b:
                continue
            for c in G[b]:
                if a >= c:
                    continue
                if c in G[a]:
                    ans += 1
    #出力
    print(ans)

if __name__ == '__main__':
    main()