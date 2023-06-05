def main():
    pin = input()
    if pin == '0000' or pin == '1111' or pin == '2222' or pin == '3333' or pin == '4444' or pin == '5555' or pin == '6666' or pin == '7777' or pin == '8888' or pin == '9999':
        print('Weak')
    elif pin[0] == pin[1] and pin[1] == pin[2] and pin[2] == pin[3]:
        print('Weak')
    elif (int(pin[0]) + 1) % 10 == int(pin[1]) and (int(pin[1]) + 1) % 10 == int(pin[2]) and (int(pin[2]) + 1) % 10 == int(pin[3]):
        print('Weak')
    else:
        print('Strong')

if __name__ == '__main__':
    main()