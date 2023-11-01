def judge_win(a, b, c, d):
    if a % d == 0:
        return True
    elif c % b == 0:
        return False
    else:
        return False
