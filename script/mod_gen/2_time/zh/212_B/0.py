def main():
    # input
    pin = input()
    # check
    if pin[0] == pin[1] == pin[2] == pin[3]:
        print('Weak')
        return
    else:
        for i in range(3):
            if pin[i] == '9':
                if pin[i+1] != '0':
                    print('Strong')
                    return
            else:
                if pin[i+1] != str(int(pin[i])+1):
                    print('Strong')
                    return
    print('Weak')
    return

if __name__ == '__main__':
    main()