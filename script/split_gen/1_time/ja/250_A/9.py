def main():
    # H,W
    h, w = map(int, input().split())
    # R,C
    r, c = map(int, input().split())
    # 答え
    ans = 0
    # 縦の端
    if r == 1 or r == h:
        ans += 1
    # 横の端
    if c == 1 or c == w:
        ans += 1
    # 縦の端でない
    if r != 1 and r != h:
        ans += 2
    # 横の端でない
    if c != 1 and c != w:
        ans += 2
    # 答えを表示
    print(ans)
