def get_input():
    N, S = map(int, input().split())
    cards = []
    for _ in range(N):
        a, b = map(int, input().split())
        cards.append((a, b))
    return N, S, cards
