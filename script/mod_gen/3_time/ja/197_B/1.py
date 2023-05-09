def main():
    h, w, x, y = map(int, input().split())
    s = [list(input()) for i in range(h)]
    x -= 1
    y -= 1
    ans = 1
    for i in range(x + 1, h):
        if s[i][y] == '.':
            ans += 1
        else:
            break
    for i in range(x - 1, -1, -1):
        if s[i][y] == '.':
            ans += 1
        else:
            break
    for j in range(y + 1, w):
        if s[x][j] == '.':
            ans += 1
        else:
            break
    for j in range(y - 1, -1, -1):
        if s[x][j] == '.':
            ans += 1
        else:
            break
    print(ans)

if __name__ == '__main__':
    main()