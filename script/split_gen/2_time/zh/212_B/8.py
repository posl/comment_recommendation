def is_weak(PIN):
    if PIN == PIN[0]*4:
        return True
    else:
        for i in range(3):
            if PIN[i] == '9' and PIN[i+1] == '0':
                return True
            elif PIN[i+1] != str(int(PIN[i])+1):
                return False
        return True
PIN = input()
