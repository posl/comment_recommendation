def main():
    H, W = map(int, input().split())
    s = [input() for _ in range(H)]
    x = 0
    y = 0
    c = 0
    while 1:
        c += 1
        if c > H * W:
            print(-1)
            break
        if s[y][x] == 'U':
            if y != 0:
                y -= 1
            else:
                print(y+1, x+1)
                break
        elif s[y][x] == 'D':
            if y != H - 1:
                y += 1
            else:
                print(y+1, x+1)
                break
        elif s[y][x] == 'L':
            if x != 0:
                x -= 1
            else:
                print(y+1, x+1)
                break
        elif s[y][x] == 'R':
            if x != W - 1:
                x += 1
            else:
                print(y+1, x+1)
                break
