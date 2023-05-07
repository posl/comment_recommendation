def checkWeak(pin):
    if pin[0] == pin[1] and pin[1] == pin[2] and pin[2] == pin[3]:
        return "Weak"
    for i in range(3):
        if int(pin[i+1]) == (int(pin[i]) + 1) % 10:
            continue
        else:
            return "Strong"
    return "Weak"
pin = input()
print(checkWeak(pin))
