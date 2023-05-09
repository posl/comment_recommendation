def calc_attack_count(health):
    if health == 1:
        return 1
    return 2 * calc_attack_count(health // 2) + 1
