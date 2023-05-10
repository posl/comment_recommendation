def main():
    pin = input()
    if (pin[0] == pin[1] == pin[2] == pin[3]) or (int(pin[1]) == (int(pin[0]) + 1) % 10 and int(pin[2]) == (int(pin[1]) + 1) % 10 and int(pin[3]) == (int(pin[2]) + 1) % 10):
        print('Weak')
    else:
        print('Strong')
