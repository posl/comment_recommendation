def get_agc(n):
    if n <= 21:
        return 'AGC%03d' % (n + 2)
    else:
        return 'AGC%03d' % (n + 1)
print(get_agc(int(input())))

if __name__ == '__main__':
    get_agc()