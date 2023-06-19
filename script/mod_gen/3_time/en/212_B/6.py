def is_weak(pin):
    return pin[0] == pin[1] == pin[2] == pin[3] or \
        (pin[0] == pin[1] == pin[2] and pin[3] == str((int(pin[2]) + 1) % 10)) or \
        (pin[1] == pin[2] == pin[3] and pin[0] == str((int(pin[3]) + 1) % 10))
pin = input()
print('Weak' if is_weak(pin) else 'Strong')
