def main():
    # H, W = map(int, input().split())
    # S = [input() for _ in range(H)]
    H, W = 5, 4
    S = ["-o--", "----", "----", "----", "-o--"]
    for i in range(H):
        for j in range(W):
            if S[i][j] == "o":
                start = (i, j)
    S[start[0]] = S[start[0]][:start[1]] + "s" + S[start[0]][start[1] + 1:]
    S[start[0]] = S[start[0]][:start[1]] + "s" + S[start[0]][start[1] + 1:]
    # print(S)
    for i in range(H):
        for j in range(W):
            if S[i][j] == "o":
                end = (i, j)
    # print(start, end)
    if start[0] == end[0]:
        print(abs(start[1] - end[1]))
    elif start[1] == end[1]:
        print(abs(start[0] - end[0]))
    else:
        print(abs(start[0] - end[0]) + abs(start[1] - end[1]))

if __name__ == '__main__':
    main()