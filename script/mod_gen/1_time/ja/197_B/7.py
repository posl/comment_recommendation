def main():
    #入力
    h, w, x, y = map(int, input().split())
    s = [input() for _ in range(h)]
    #マス (x, y) から見えるマスの数を数える
    ans = 1
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        i, j = x - 1, y - 1
        while True:
            i += dx
            j += dy
            if not (0 <= i < h and 0 <= j < w):
                break
            if s[i][j] == '#':
                break
            ans += 1
    #出力
    print(ans)

if __name__ == '__main__':
    main()