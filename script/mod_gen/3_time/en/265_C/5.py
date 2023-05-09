def main():
    h, w = map(int, input().split())
    g = [input() for _ in range(h)]
    i, j = 0, 0
    for _ in range(h * w):
        if g[i][j] == "U":
            i -= 1
        elif g[i][j] == "D":
            i += 1
        elif g[i][j] == "L":
            j -= 1
        elif g[i][j] == "R":
            j += 1
        if i < 0 or i >= h or j < 0 or j >= w:
            print(i + 1, j + 1)
            break
    else:
        print(-1)

if __name__ == '__main__':
    main()