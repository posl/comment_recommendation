def main():
    h, w = map(int, input().split())
    c = []
    for i in range(h):
        c.append(input())
    ans = 0
    x = 0
    y = 0
    while True:
        if x == w - 1 and y == h - 1:
            ans += 1
            break
        if x == w - 1:
            if c[y + 1][x] == ".":
                y += 1
                ans += 1
            else:
                ans += 1
                break
        elif y == h - 1:
            if c[y][x + 1] == ".":
                x += 1
                ans += 1
            else:
                ans += 1
                break
        else:
            if c[y + 1][x] == "." and c[y][x + 1] == ".":
                if c[y + 1][x + 1] == ".":
                    x += 1
                    y += 1
                    ans += 2
                else:
                    ans += 1
                    break
            elif c[y + 1][x] == ".":
                y += 1
                ans += 1
            elif c[y][x + 1] == ".":
                x += 1
                ans += 1
            else:
                ans += 1
                break
    print(ans)
