def main():
    pin = input()
    if pin[0] == pin[1] == pin[2] == pin[3]:
        print('Weak')
    elif int(pin[0]) + 1 == int(pin[1]) and int(pin[1]) + 1 == int(pin[2]) and int(pin[2]) + 1 == int(pin[3]):
        print('Weak')
    elif int(pin[0]) + 1 == int(pin[1]) and int(pin[1]) + 1 == int(pin[2]) and int(pin[3]) == 0:
        print('Weak')
    elif int(pin[0]) == 9 and int(pin[1]) == 0 and int(pin[2]) + 1 == int(pin[3]):
        print('Weak')
    else:
        print('Strong')

if __name__ == '__main__':
    main()