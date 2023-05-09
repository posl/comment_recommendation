def agc(n):
    if n < 42:
        return 'AGC' + str(n).zfill(3)
    else:
        return 'AGC' + str(n + 1).zfill(3)

if __name__ == '__main__':
    agc()