def main():
    h, w, x, y = map(int, input().split())
    s = []
    for i in range(h):
        s.append(input())
    ans = 1
    for i in range(y-2, -1, -1):
        if s[x-1][i] == "#":
            break
        ans += 1
    for i in range(y, w):
        if s[x-1][i] == "#":
            break
        ans += 1
    for i in range(x-2, -1, -1):
        if s[i][y-1] == "#":
            break
        ans += 1
    for i in range(x, h):
        if s[i][y-1] == "#":
            break
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()