def main():
    h, w = map(int, input().split())
    s = []
    for i in range(h):
        s.append(input())
    for i in range(h):
        for j in range(w):
            if s[i][j] == 'o':
                sx, sy = i, j
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == 'o':
                ans = max(ans, abs(sx - i) + abs(sy - j))
    print(ans)
