def isWeak(pin):
    if pin[0] == pin[1] == pin[2] == pin[3]:
        return True
    for i in range(3):
        if pin[i] == '9':
            if pin[i+1] != '0':
                return False
        elif int(pin[i]) + 1 != int(pin[i+1]):
            return False
    return True
pin = input()

if __name__ == '__main__':
    isWeak()