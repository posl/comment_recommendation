def moveStr(str, n):
    if n == 0:
        return str
    result = ''
    for s in str:
        num = ord(s) + n
        if num > 90:
            num = num - 26
        result = result + chr(num)
    return result

if __name__ == '__main__':
    moveStr()