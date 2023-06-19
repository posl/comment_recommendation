def calc_attack_times(h):
    if h == 1:
        return 1
    else:
        return 2 * calc_attack_times(h // 2) + 1
h = int(input())
print(calc_attack_times(h))
