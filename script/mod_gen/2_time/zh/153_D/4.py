def cal_attack_times(hp):
    if hp == 1:
        return 1
    else:
        return 2 * cal_attack_times(hp // 2) + 1

if __name__ == '__main__':
    cal_attack_times()