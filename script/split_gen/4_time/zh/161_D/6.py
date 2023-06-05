def isLuckyNumber(n):
    if n < 10:
        return True
    else:
        while n > 9:
            n1 = n % 10
            n2 = n // 10 % 10
            if abs(n1 - n2) > 1:
                return False
            n = n // 10
        return True
