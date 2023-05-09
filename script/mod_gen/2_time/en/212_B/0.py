def main():
    pin = input()
    if pin[0] == pin[1] == pin[2] == pin[3]:
        print('Weak')
    elif pin[0] == '9' and pin[1] == '0' and pin[2] == '1' and pin[3] == '2':
        print('Weak')
    elif pin[0] == '0' and pin[1] == '1' and pin[2] == '2' and pin[3] == '3':
        print('Weak')
    elif pin[0] == '1' and pin[1] == '2' and pin[2] == '3' and pin[3] == '4':
        print('Weak')
    elif pin[0] == '2' and pin[1] == '3' and pin[2] == '4' and pin[3] == '5':
        print('Weak')
    elif pin[0] == '3' and pin[1] == '4' and pin[2] == '5' and pin[3] == '6':
        print('Weak')
    elif pin[0] == '4' and pin[1] == '5' and pin[2] == '6' and pin[3] == '7':
        print('Weak')
    elif pin[0] == '5' and pin[1] == '6' and pin[2] == '7' and pin[3] == '8':
        print('Weak')
    elif pin[0] == '6' and pin[1] == '7' and pin[2] == '8' and pin[3] == '9':
        print('Weak')
    else:
        print('Strong')
main()

if __name__ == '__main__':
    main()