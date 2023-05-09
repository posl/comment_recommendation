def main():
    h, w, x, y = map(int, input().split())
    x = x - 1
    y = y - 1
    s = []
    for i in range(h):
        s.append(input())
    count = 0
    for i in range(x, h):
        if s[i][y] == '#':
            break
        else:
            count += 1
    for i in range(x-1, -1, -1):
        if s[i][y] == '#':
            break
        else:
            count += 1
    for i in range(y, w):
        if s[x][i] == '#':
            break
        else:
            count += 1
    for i in range(y-1, -1, -1):
        if s[x][i] == '#':
            break
        else:
            count += 1
    print(count-3)
