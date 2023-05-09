def calc_attack_count(hp):
    if hp == 1:
        return 1
    else:
        return 2 * calc_attack_count(hp // 2) + 1

if __name__ == '__main__':
    calc_attack_count()