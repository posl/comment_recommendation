def check_yymm(mm):
    if (mm >= 1 and mm <= 12):
        return True
    else:
        return False

if __name__ == '__main__':
    check_yymm()