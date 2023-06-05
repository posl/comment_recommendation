def attack_count(h, a):
    count = 0
    while h > 0:
        h = h - a
        count = count + 1
    return count
