def main():
    h, w, x, y = map(int, input().split())
    x -= 1
    y -= 1
    S = [input() for _ in range(h)]
    ans = 1
    for i in range(x+1, h):
        if S[i][y] == '#':
            break
        ans += 1
    for i in range(x-1, -1, -1):
        if S[i][y] == '#':
            break
        ans += 1
    for i in range(y+1, w):
        if S[x][i] == '#':
            break
        ans += 1
    for i in range(y-1, -1, -1):
        if S[x][i] == '#':
            break
        ans += 1
    print(ans)
