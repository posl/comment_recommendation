def calc_attack_count(h):
    if h == 1:
        return 1
    else:
        return 2 * calc_attack_count(h // 2) + 1
h = int(input())
print(calc_attack_count(h))

if __name__ == '__main__':
    calc_attack_count()