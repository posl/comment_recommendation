def replace(s):
    result = ''
    flag = 0
    for c in s:
        if c == '"':
            if flag == 0:
                flag = 1
            else:
                flag = 0
        if c == ',' and flag == 0:
            result += '.'
        else:
            result += c
    return result

if __name__ == '__main__':
    replace()