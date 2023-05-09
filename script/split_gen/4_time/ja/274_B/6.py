def main():
    # 標準入力から1行取得
    line = input()
    # 空白で分割して2つの整数として扱う
    H, W = map(int, line.split())
    # 標準入力からH行取得してリストに格納
    S = [input() for i in range(H)]
    # 各列について、#の数を数える
    ans = [0] * W
    for i in range(W):
        for j in range(H):
            if S[j][i] == '#':
                ans[i] += 1
    # 結果を出力
    print(*ans)
