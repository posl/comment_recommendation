def compare_power(a,b,c):
    if (a == b):
        return '='
    elif (c % 2 == 0):
        if (abs(a) == abs(b)):
            return '='
        elif (abs(a) < abs(b)):
            return '<'
        else:
            return '>'
    elif (c % 2 == 1):
        if (a < b):
            return '<'
        else:
            return '>'
    else:
        return 'ERROR'

if __name__ == '__main__':
    compare_power()