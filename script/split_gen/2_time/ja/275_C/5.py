def main():
    # 入力
    S = [input() for _ in range(9)]
    # 処理
    ans = 0
    for i in range(7):
        for j in range(7):
            if S[i][j] == "#" and S[i][j+1] == "#" and S[i+1][j] == "#" and S[i+1][j+1] == "#":
                ans += 1
    # 出力
    print(ans)
