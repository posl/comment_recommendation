def solve():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if s[i][j] == "o":
                x1, y1 = i, j
            if s[i][j] == "o":
                x2, y2 = i, j
    print(max(abs(x1-x2), abs(y1-y2)))

if __name__ == '__main__':
    solve()