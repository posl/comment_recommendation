def main():
    pin = input()
    if pin[0] == pin[1] and pin[1] == pin[2] and pin[2] == pin[3]:
        print('Weak')
    else:
        for i in range(3):
            if (int(pin[i]) + 1) % 10 != int(pin[i+1]):
                break
        else:
            print('Weak')
            return
        print('Strong')

if __name__ == '__main__':
    main()