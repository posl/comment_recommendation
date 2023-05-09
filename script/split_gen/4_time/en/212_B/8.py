def main():
    pin = input()
    if pin[0] == pin[1] == pin[2] == pin[3]:
        print('Weak')
    else:
        if int(pin[0]) == int(pin[1]) + 1 or int(pin[0]) == 0 and int(pin[1]) == 9:
            if int(pin[1]) == int(pin[2]) + 1 or int(pin[1]) == 0 and int(pin[2]) == 9:
                if int(pin[2]) == int(pin[3]) + 1 or int(pin[2]) == 0 and int(pin[3]) == 9:
                    print('Weak')
                else:
                    print('Strong')
            else:
                print('Strong')
        else:
            print('Strong')
