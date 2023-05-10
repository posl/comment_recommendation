def main():
    # 標準入力から値を取得する
    h, w, x, y = map(int, input().split())
    s = [list(input()) for i in range(h)]
    x -= 1
    y -= 1
    ans = 0
    # 上方向
    for i in range(x-1, -1, -1):
        if s[i][y] == "#":
            break
        ans += 1
    # 下方向
    for i in range(x+1, h):
        if s[i][y] == "#":
            break
        ans += 1
    # 左方向
    for i in range(y-1, -1, -1):
        if s[x][i] == "#":
            break
        ans += 1
    # 右方向
    for i in range(y+1, w):
        if s[x][i] == "#":
            break
        ans += 1
    # マス (x, y) 自身を含む
    ans += 1
    # 結果出力
    print(ans)
