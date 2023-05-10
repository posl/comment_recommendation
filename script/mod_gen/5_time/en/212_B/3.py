def weak_or_strong(pin):
    if pin[0] == pin[1] and pin[1] == pin[2] and pin[2] == pin[3]:
        return "Weak"
    else:
        if (int(pin[0]) + 1) % 10 == int(pin[1]) and (int(pin[1]) + 1) % 10 == int(pin[2]) and (int(pin[2]) + 1) % 10 == int(pin[3]):
            return "Weak"
        else:
            return "Strong"

if __name__ == '__main__':
    weak_or_strong()