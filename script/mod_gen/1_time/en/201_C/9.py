def get_pin_count(pin):
    if len(pin) == 4:
        return 1
    elif pin[0] == 'o':
        return 10 * get_pin_count(pin[1:])
    elif pin[0] == 'x':
        return 9 * get_pin_count(pin[1:])
    else:
        return 10 * get_pin_count(pin[1:]) + 9 * get_pin_count(pin[1:])

if __name__ == '__main__':
    get_pin_count()