def agc(n):
    if n < 43:
        return 'AGC' + str(n).zfill(3)
    else:
        return 'AGC' + str(n+1).zfill(3)
