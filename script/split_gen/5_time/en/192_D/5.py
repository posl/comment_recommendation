def get_max_digit(s):
    max_digit = 0
    for i in range(len(s)):
        if int(s[i]) > max_digit:
            max_digit = int(s[i])
    return max_digit
