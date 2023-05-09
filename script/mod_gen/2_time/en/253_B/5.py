def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if s[i][j] == "o":
                x, y = i, j
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == "o":
                ans = max(ans, abs(i - x) + abs(j - y))
    print(ans)

if __name__ == '__main__':
    main()