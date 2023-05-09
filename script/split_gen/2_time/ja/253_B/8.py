def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    # 二つの駒の位置を求める
    for i in range(H):
        for j in range(W):
            if S[i][j] == "o":
                x0, y0 = i, j
            elif S[i][j] == "o":
                x1, y1 = i, j
    # 二つの駒の距離を求める
    ans = abs(x0 - x1) + abs(y0 - y1)
    print(ans)
