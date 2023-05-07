def time(k):
    hh = 21 + (k // 60)
    mm = k % 60
    if hh > 23:
        hh -= 24
    if mm < 10:
        mm = "0" + str(mm)
    return str(hh) + ":" + str(mm)

if __name__ == '__main__':
    time()