def calc_attack_count(h):
    if h==1:
        return 1
    else:
        return 1+2*calc_attack_count(h//2)
