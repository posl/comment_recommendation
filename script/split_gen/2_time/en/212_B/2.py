def main():
    pin = input()
    if pin[0] == pin[1] == pin[2] == pin[3]:
        print('Weak')
        return
    for i in range(3):
        if int(pin[i+1]) - int(pin[i]) == 1 or int(pin[i+1]) - int(pin[i]) == -9:
            continue
        else:
            print('Strong')
            return
    print('Weak')
