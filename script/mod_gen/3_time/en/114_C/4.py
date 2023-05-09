def isShichiGoSan(n):
    nstr = str(n)
    if nstr.count('7') > 0 and nstr.count('5') > 0 and nstr.count('3') > 0:
        return True
    else:
        return False

if __name__ == '__main__':
    isShichiGoSan()