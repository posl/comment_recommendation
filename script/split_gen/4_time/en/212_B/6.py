def main():
    pin = input()
    weak = True
    if pin[0] == pin[1] == pin[2] == pin[3]:
        weak = True
    else:
        weak = False
        if pin[0] == '9' and pin[1] == '0' and pin[2] == '1' and pin[3] == '2':
            weak = True
        else:
            if pin[1] == str((int(pin[0])+1)%10) and pin[2] == str((int(pin[1])+1)%10) and pin[3] == str((int(pin[2])+1)%10):
                weak = True
    if weak:
        print('Weak')
    else:
        print('Strong')
