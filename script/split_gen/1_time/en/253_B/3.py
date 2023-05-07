def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if s[i][j] == 'o':
                x = i
                y = j
                break
    ans = 0
    for i in range(h):
        ans = max(ans, abs(x - i))
    for j in range(w):
        ans = max(ans, abs(y - j))
    print(ans)
