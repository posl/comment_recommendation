def calcMP(target, bambooList):
    if target in bambooList:
        return 0
    if target < min(bambooList):
        return 9999
    if target < 2:
        return 9999
    result = 9999
    for b in bambooList:
        if b < target:
            result = min(result, 1 + calcMP(target - b, bambooList))
    return result
