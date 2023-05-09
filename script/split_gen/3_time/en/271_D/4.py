def get_input():
    n, s = map(int, input().split())
    cards = []
    for _ in range(n):
        cards.append(list(map(int, input().split())))
    return n, s, cards
