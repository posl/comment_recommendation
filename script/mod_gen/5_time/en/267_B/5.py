def split_pins(pins):
    if pins[0] == '0':
        if pins[1] == '1' and pins[2] == '1' and pins[3] == '1' and pins[4] == '1':
            return True
        elif pins[5] == '1' and pins[6] == '1' and pins[7] == '1' and pins[8] == '1' and pins[9] == '1':
            return True
        else:
            return False
    else:
        return False

if __name__ == '__main__':
    split_pins()