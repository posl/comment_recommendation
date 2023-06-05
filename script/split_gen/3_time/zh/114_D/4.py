def is_seven_five(n):
    cnt = 0
    for i in range(1, n+1):
        if n % i == 0:
            cnt += 1
    if cnt == 75:
        return True
    else:
        return False
