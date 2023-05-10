def is_weak(pin):
    if len(set(pin)) == 1:
        return True
    for i in range(len(pin) - 1):
        if int(pin[i]) + 1 != int(pin[i + 1]) and not (pin[i] == '9' and pin[i + 1] == '0'):
            return False
    return True
