def is_split(pins):
    if pins[0] == '0':
        return False
    i = 1
    while i < 10:
        if pins[i] == '1':
            break
        i += 1
    if i == 10:
        return False
    i += 1
    while i < 10:
        if pins[i] == '1':
            return True
        i += 1
    return False
pins = input()
