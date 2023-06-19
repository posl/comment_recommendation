def isWeak(pin):
    if pin[0] == pin[1] and pin[1] == pin[2] and pin[2] == pin[3]:
        return True
    elif (int(pin[1]) - int(pin[0]) + 10) % 10 == 1 and (int(pin[2]) - int(pin[1]) + 10) % 10 == 1 and (int(pin[3]) - int(pin[2]) + 10) % 10 == 1:
        return True
    else:
        return False
