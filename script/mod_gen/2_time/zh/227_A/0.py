def get_last_card(n, k, a):
    card = 0
    for i in range(1, k+1):
        if card == 0:
            card = a
        else:
            card = (card + 1) % (n + 1)
            if card == 0:
                card = 1
    return card

if __name__ == '__main__':
    get_last_card()