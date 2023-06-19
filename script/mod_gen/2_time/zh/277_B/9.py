def check(n, cards):
    if n != len(cards):
        return False
    for i in range(n):
        if len(cards[i]) != 2:
            return False
    for i in range(n):
        if cards[i][0] not in ('H', 'D', 'C', 'S'):
            return False
        if cards[i][1] not in ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J','Q', 'K'):
            return False
    for i in range(n):
        for j in range(i+1, n):
            if cards[i] == cards[j]:
                return False
    return True

if __name__ == '__main__':
    check()