def find_lost_card(N, A):
    cards = {}
    for a in A:
        if a in cards:
            cards[a] += 1
        else:
            cards[a] = 1
    for i in range(1, N+1):
        if i not in cards or cards[i] < 4:
            return i

if __name__ == '__main__':
    find_lost_card()