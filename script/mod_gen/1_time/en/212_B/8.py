def main():
    #input
    pin = input()
    #output
    if pin[0] == pin[1] == pin[2] == pin[3]:
        print('Weak')
    elif int(pin[0]) == (int(pin[1])-1)%10 == (int(pin[2])-1)%10 == (int(pin[3])-1)%10:
        print('Weak')
    else:
        print('Strong')
main()

if __name__ == '__main__':
    main()