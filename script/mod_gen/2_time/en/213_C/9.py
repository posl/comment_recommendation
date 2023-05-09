def main():
    H, W, N = map(int, input().split())
    cards = [tuple(map(int, input().split())) for _ in range(N)]
    cards.sort(key=lambda x: x[0])
    row = 0
    for i in range(N):
        if cards[i][0] != cards[row][0]:
            row = i
        cards[i] = (row+1, cards[i][1])
    cards.sort(key=lambda x: x[1])
    col = 0
    for i in range(N):
        if cards[i][1] != cards[col][1]:
            col = i
        cards[i] = (cards[i][0], col+1)
    cards.sort(key=lambda x: x[0])
    for c in cards:
        print(c[0], c[1])
main()

if __name__ == '__main__':
    main()