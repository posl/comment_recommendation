def main():
    pin = input()
    weak = True
    if pin[0] == pin[1] and pin[1] == pin[2] and pin[2] == pin[3]:
        weak = True
    elif pin[0] == '9' and pin[1] == '0' and pin[2] == '1':
        weak = True
    elif pin[0] == '0' and pin[1] == '9' and pin[2] == '8':
        weak = True
    elif pin[0] == pin[1] and pin[1] == pin[2]:
        weak = True
    elif pin[1] == pin[2] and pin[2] == pin[3]:
        weak = True
    else:
        weak = False
    if weak:
        print('Weak')
    else:
        print('Strong')

if __name__ == '__main__':
    main()