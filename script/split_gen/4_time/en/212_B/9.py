def checkWeak(pin):
    if pin == '0000':
        return True
    if pin[0] == pin[1] == pin[2] == pin[3]:
        return True
    if int(pin[1]) == (int(pin[0])+1)%10 and int(pin[2]) == (int(pin[1])+1)%10 and int(pin[3]) == (int(pin[2])+1)%10:
        return True
    return False
pin = input()
