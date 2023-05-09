def main():
    H, W, N = map(int, input().split())
    cards = [list(map(int, input().split())) for _ in range(N)]
    cards.sort(key = lambda x: x[0])
    cards.sort(key = lambda x: x[1])
    cards.sort(key = lambda x: x[0] + x[1])
    cards.sort(key = lambda x: x[0] * x[1])
    cards.sort(key = lambda x: x[0] + x[1])
    for i in range(N):
        print(cards[i][0], cards[i][1])

if __name__ == '__main__':
    main()