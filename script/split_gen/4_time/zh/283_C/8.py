def func(s):
    result = 0
    for i in range(len(s)):
        if s[i] == '0':
            result += 1
    return result + 1
