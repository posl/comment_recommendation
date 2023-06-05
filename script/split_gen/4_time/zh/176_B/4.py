def is_multiple_of_9(s):
    sum = 0
    for i in range(len(s)):
        sum += int(s[i])
    if sum % 9 == 0:
        return True
    else:
        return False
