def main():
    N = int(input())
    cards = []
    for i in range(N):
        cards.append(input())
    if len(set(cards)) != N:
        print('No')
        return
    for c in cards:
        if c[0] not in ['H', 'D', 'C', 'S']:
            print('No')
            return
        if c[1] not in ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']:
            print('No')
            return
    print('Yes')
