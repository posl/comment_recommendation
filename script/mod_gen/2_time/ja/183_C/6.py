def main():
    # 入力
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]
    # ルートの初期化
    route = [0]
    # 探索
    ans = dfs(N, K, T, route)
    # 出力
    print(ans)

if __name__ == '__main__':
    main()