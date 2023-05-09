def main():
    # 入力
    N, M = list(map(int, input().split()))
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    # 処理
    def is_ok(x):
        for t in T:
            if t == x:
                return False
        return True
    def dfs(s):
        if len(s) > 16:
            return
        if is_ok(s):
            print(s)
            exit()
        for i in range(N):
            dfs(s + "_" + S[i])
        return
    # 出力
    dfs("")
    print(-1)

if __name__ == '__main__':
    main()