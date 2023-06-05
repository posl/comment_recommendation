def count(s):
    result = {}
    for i in s:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result
