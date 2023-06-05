def is_9_multiple(n):
    sum = 0
    for i in n:
        sum += int(i)
    if sum % 9 == 0:
        return True
    else:
        return False
