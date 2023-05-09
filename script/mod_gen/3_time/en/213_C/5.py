def main():
    H, W, N = map(int, input().split())
    cards = [list(map(int, input().split())) for _ in range(N)]
    cards.sort(key=lambda x: x[0])
    cards.sort(key=lambda x: x[1])
    row = 1
    col = 1
    row_list = []
    col_list = []
    for i in range(N):
        while row < cards[i][0]:
            row_list.append(row)
            row += 1
        while col < cards[i][1]:
            col_list.append(col)
            col += 1
        row_list.append(cards[i][0])
        col_list.append(cards[i][1])
        row += 1
        col += 1
    while row <= H:
        row_list.append(row)
        row += 1
    while col <= W:
        col_list.append(col)
        col += 1
    for i in range(N):
        print(row_list[i], col_list[i])

if __name__ == '__main__':
    main()