def checkShichiGoSanNumber(num):
    s = str(num)
    return s.count('7') > 0 and s.count('5') > 0 and s.count('3') > 0

if __name__ == '__main__':
    checkShichiGoSanNumber()