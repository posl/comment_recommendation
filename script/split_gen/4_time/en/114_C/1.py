def isShichiGoSan(num):
    numStr = str(num)
    if "7" in numStr and "5" in numStr and "3" in numStr:
        return True
    else:
        return False
