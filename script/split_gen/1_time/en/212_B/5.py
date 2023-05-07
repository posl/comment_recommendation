def is_weak(pin):
    return pin[0] == pin[1] == pin[2] == pin[3] or \
           pin[0] == pin[1] == pin[2] or \
           pin[1] == pin[2] == pin[3] or \
           pin[0] == pin[1] or \
           pin[1] == pin[2] or \
           pin[2] == pin[3]
pin = input()
