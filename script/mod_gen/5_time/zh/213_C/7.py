def main():
    H, W, N = map(int, input().split())
    cards = []
    for i in range(N):
        A, B = map(int, input().split())
        cards.append([A, B, i+1])
    cards.sort(key=lambda x: x[0])
    for i in range(N):
        cards[i][0] = i + 1
    cards.sort(key=lambda x: x[1])
    for i in range(N):
        cards[i][1] = i + 1
    cards.sort(key=lambda x: x[2])
    for i in range(N):
        print(cards[i][0], cards[i][1])
    return 0

if __name__ == '__main__':
    main()