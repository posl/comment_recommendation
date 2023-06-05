def attack_num(h, k):
    h.sort(reverse=True)
    return sum(h[k:])

if __name__ == '__main__':
    attack_num()