def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    count = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                count += 1
    if count == 0:
        print(0)
        exit()
    elif count == 1:
        print(1)
        exit()
    else:
        pass
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                start = (i, j)
                break
        else:
            continue
        break
    x, y = start
    next = (x, y+1)
    if next[1] >= W:
        next = (x+1, 0)
    else:
        pass
    count = 1
    while next != start:
        if S[next[0]][next[1]] == "#":
            count += 1
            x, y = next
            next = (x, y+1)
            if next[1] >= W:
                next = (x+1, 0)
            else:
                pass
        else:
            x, y = next
            next = (x, y+1)
            if next[1] >= W:
                next = (x+1, 0)
            else:
                pass
    print(count)

if __name__ == '__main__':
    main()