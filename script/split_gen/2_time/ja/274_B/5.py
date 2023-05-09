def main():
    # 標準入力の取得
    H, W = map(int, input().split())
    C = [input() for i in range(H)]
    # 出力
    for i in range(W):
        count = 0
        for j in range(H):
            if C[j][i] == '#':
                count += 1
        print(count)
