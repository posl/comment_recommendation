def main():
    # Get input
    h, w, x, y = map(int, input().split())
    s = [input() for i in range(h)]
    # Count visible squares
    count = 1
    for i in range(x - 2, -1, -1):
        if s[i][y - 1] == "#":
            break
        count += 1
    for i in range(x, h):
        if s[i][y - 1] == "#":
            break
        count += 1
    for i in range(y - 2, -1, -1):
        if s[x - 1][i] == "#":
            break
        count += 1
    for i in range(y, w):
        if s[x - 1][i] == "#":
            break
        count += 1
    # Print answer
    print(count)

if __name__ == '__main__':
    main()