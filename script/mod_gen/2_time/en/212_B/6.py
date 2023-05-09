def isWeak(pin):
    for i in range(1,4):
        if pin[i] != pin[i-1]:
            break
    else:
        return True
    for i in range(1,4):
        if pin[i] != str((int(pin[i-1])+1)%10):
            return False
    return True
pin = input()

if __name__ == '__main__':
    isWeak()