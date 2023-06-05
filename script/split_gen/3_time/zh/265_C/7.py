def main():
    h, w = map(int, input().split())
    g = []
    for i in range(h):
        g.append(input())
    i, j = 0, 0
    while True:
        if g[i][j] == "U" and i != 0:
            i -= 1
        elif g[i][j] == "D" and i != h - 1:
            i += 1
        elif g[i][j] == "L" and j != 0:
            j -= 1
        elif g[i][j] == "R" and j != w - 1:
            j += 1
        else:
            break
    if i == 0 and j == 0:
        print(-1)
    else:
        print(i + 1, j + 1)
