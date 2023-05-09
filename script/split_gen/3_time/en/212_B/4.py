def is_weak_pin(pin):
    if pin[0] == pin[1] == pin[2] == pin[3]:
        return True
    for i in range(3):
        if pin[i+1] != str((int(pin[i])+1)%10):
            return False
    return True
pin = input()
