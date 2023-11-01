def judge(n):
    if n % 10 == 7:
        return True
    elif n >= 10:
        return judge(n // 10)
    else:
        return False
