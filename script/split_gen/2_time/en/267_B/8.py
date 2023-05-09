def check_split(pins):
    if pins[0] == '0':
        return False
    else:
        left = []
        right = []
        for i in range(1, 5):
            if pins[i] == '1':
                left.append(i)
            if pins[10-i] == '1':
                right.append(10-i)
        if len(left) == 0 or len(right) == 0:
            return False
        else:
            for i in range(1, 5):
                if pins[i] == '0' and pins[10-i] == '0':
                    return True
            return False
