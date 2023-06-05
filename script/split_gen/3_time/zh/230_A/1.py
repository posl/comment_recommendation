def get_AGC_name(n):
    if n > 42:
        return 'AGC' + str(n + 1).zfill(3)
    elif n == 42:
        return 'AGC043'
    elif n > 19:
        return 'AGC' + str(n).zfill(3)
    elif n == 19:
        return 'AGC020'
    else:
        return 'AGC' + str(n).zfill(3)
