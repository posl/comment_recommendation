def main():
    pin = input()
    if pin[0] == pin[1] == pin[2] == pin[3]:
        print('Weak')
        return
    if pin[0] == '9' and pin[1] == '0':
        if pin[2] == '1' and pin[3] == '2':
            print('Weak')
            return
    if pin[0] == '0' and pin[1] == '1':
        if pin[2] == '2' and pin[3] == '3':
            print('Weak')
            return
    if pin[0] == '1' and pin[1] == '2':
        if pin[2] == '3' and pin[3] == '4':
            print('Weak')
            return
    if pin[0] == '2' and pin[1] == '3':
        if pin[2] == '4' and pin[3] == '5':
            print('Weak')
            return
    if pin[0] == '3' and pin[1] == '4':
        if pin[2] == '5' and pin[3] == '6':
            print('Weak')
            return
    if pin[0] == '4' and pin[1] == '5':
        if pin[2] == '6' and pin[3] == '7':
            print('Weak')
            return
    if pin[0] == '5' and pin[1] == '6':
        if pin[2] == '7' and pin[3] == '8':
            print('Weak')
            return
    if pin[0] == '6' and pin[1] == '7':
        if pin[2] == '8' and pin[3] == '9':
            print('Weak')
            return
    if pin[0] == '7' and pin[1] == '8':
        if pin[2] == '9' and pin[3] == '0':
            print('Weak')
            return
    if pin[0] == '8' and pin[1] == '9':
        if pin[2] == '0' and pin[3] == '1':
            print('Weak')
            return
    print('Strong

if __name__ == '__main__':
    main()