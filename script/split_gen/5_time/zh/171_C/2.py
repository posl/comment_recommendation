def calc_name(num):
    if num <= 26:
        return chr(num + 96)
    elif num <= 702:
        return calc_name((num - 1) // 26) + calc_name((num - 1) % 26 + 1)
    elif num <= 18278:
        return calc_name((num - 1) // 676) + calc_name((num - 1) % 676 + 1)
    else:
        return calc_name((num - 1) // 17576) + calc_name((num - 1) % 17576 + 1)
