def weak(pin):
    if pin[0] == pin[1] == pin[2] == pin[3]:
        return True
    for i in range(3):
        if (int(pin[i]) + 1) % 10 != int(pin[i + 1]):
            return False
    return True
pin = input()
