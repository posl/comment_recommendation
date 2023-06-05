def move_people(s):
    if s == '0000':
        return '0000'
    elif s == '1111':
        return '0111'
    elif s == '1011':
        return '0101'
    elif s == '1101':
        return '0110'
    elif s == '1110':
        return '1011'
    elif s == '0111':
        return '1011'
    elif s == '1010':
        return '0101'
    elif s == '0101':
        return '1010'
    elif s == '1100':
        return '0110'
    elif s == '0011':
        return '1001'
    elif s == '1001':
        return '0010'
    elif s == '1000':
        return '0001'
    elif s == '0001':
        return '1000'
    elif s == '0010':
        return '0001'
    elif s == '0100':
        return '0010'
    elif s == '0001':
        return '1000'
    elif s == '1000':
        return '0001'
    elif s == '0010':
        return '0001'

if __name__ == '__main__':
    move_people()