def calc_attack_count(hp):
    if hp == 1:
        return 1
    else:
        return 2 * calc_attack_count(hp // 2) + 1
hp = int(input())
print(calc_attack_count(hp))
