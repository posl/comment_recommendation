def get_result(n, x, s):
    result = x
    for i in range(n):
        if s[i] == 'o':
            result += 1
        else:
            if result > 0:
                result -= 1
    return result
