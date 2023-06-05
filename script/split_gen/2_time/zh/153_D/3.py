def attack_num(h, k):
    h.sort(reverse=True)
    return sum(h[k:])
