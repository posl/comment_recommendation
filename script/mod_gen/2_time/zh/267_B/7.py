def dayToSat(s):
    if s == '星期一':
        return 5
    elif s == '星期二':
        return 4
    elif s == '星期三':
        return 3
    elif s == '星期四':
        return 2
    elif s == '星期五':
        return 1
    else:
        return 0

if __name__ == '__main__':
    dayToSat()