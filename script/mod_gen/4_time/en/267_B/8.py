def is_split(pins):
    if pins[0] == '0':
        return False
    else:
        left = False
        right = False
        for i in range(1, 5):
            if pins[i] == '1':
                left = True
        for i in range(6, 10):
            if pins[i] == '1':
                right = True
        return left and right

if __name__ == '__main__':
    is_split()