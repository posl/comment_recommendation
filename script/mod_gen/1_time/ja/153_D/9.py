def count_attack(h):
    if h == 1:
        return 1
    else:
        return 1 + 2 * count_attack(h//2)

if __name__ == '__main__':
    count_attack()