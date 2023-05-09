def main():
    N, S = map(int, input().split())
    cards = []
    for i in range(N):
        a, b = map(int, input().split())
        cards.append([a, b])
    print(cards)
    print(N, S)
