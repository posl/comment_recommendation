def is_multiple_of_9(s):
    sum = 0
    for i in range(len(s)):
        sum += int(s[i])
    return sum % 9 == 0
