def calc_attack_times(H):
    if H == 1:
        return 1
    else:
        return 1 + 2 * calc_attack_times(H // 2)
H = int(input())
print(calc_attack_times(H))

if __name__ == '__main__':
    calc_attack_times()