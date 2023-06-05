def isLuckyNumber(n):
    if n < 10:
        return True
    n = str(n)
    for i in range(len(n)-1):
        if abs(int(n[i]) - int(n[i+1])) > 1:
            return False
    return True
