def main():
    pin = input()
    if pin[0] == pin[1] == pin[2] == pin[3]:
        print('Weak')
    else:
        for i in range(3):
            if pin[i] == '9':
                if pin[i+1] != '0':
                    print('Strong')
                    return
            elif pin[i+1] != str(int(pin[i]) + 1):
                print('Strong')
                return
        print('Weak')
