def checkWeakness(pin):
    if pin[0] == pin[1] == pin[2] == pin[3]:
        return True
    else:
        for i in range(0, 3):
            if pin[i+1] == str(int(pin[i]) + 1):
                continue
            else:
                return False
        return True
pin = input()

if __name__ == '__main__':
    checkWeakness()