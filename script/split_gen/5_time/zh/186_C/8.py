def is_valid(num):
    for i in range(len(str(num))):
        if str(num)[i] == '7':
            return False
    for i in range(len(oct(num))):
        if oct(num)[i] == '7':
            return False
    return True
