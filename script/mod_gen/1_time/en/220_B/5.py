def baseToDec (base, num):
    dec = 0
    for i in range(len(num)):
        dec += int(num[i]) * pow(base, len(num) - 1 - i)
    return dec

if __name__ == '__main__':
    baseToDec()