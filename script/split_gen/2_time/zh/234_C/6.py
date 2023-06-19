def make_num(num):
    if num == 0:
        return '0'
    elif num == 2:
        return '2'
    else:
        return make_num(num//2) + str(num%2)
