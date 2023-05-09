def rotate(s):
    reverse = s[::-1]
    result = ''
    for i in reverse:
        if i == '0':
            result += '0'
        elif i == '1':
            result += '1'
        elif i == '6':
            result += '9'
        elif i == '8':
            result += '8'
        elif i == '9':
            result += '6'
    return result

if __name__ == '__main__':
    rotate()