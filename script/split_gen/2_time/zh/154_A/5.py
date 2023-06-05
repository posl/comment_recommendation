def attack(h):
    if h == 1:
        return 1
    else:
        return 2 * attack(h // 2) + 1
