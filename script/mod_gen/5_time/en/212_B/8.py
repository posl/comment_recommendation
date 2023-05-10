def isWeakPin(pin):
    if all(pin[0] == x for x in pin):
        return True
    for i in range(1, 4):
        if int(pin[i]) != (int(pin[i-1]) + 1) % 10:
            return False
    return True
pin = input()

if __name__ == '__main__':
    isWeakPin()