def main():
    pin = input()
    if pin[0] == pin[1] and pin[1] == pin[2] and pin[2] == pin[3]:
        print("Weak")
        return
    for i in range(3):
        if pin[i] == '9':
            if pin[i+1] != '0':
                print("Strong")
                return
        elif str(int(pin[i]) + 1) != pin[i+1]:
            print("Strong")
            return
    print("Weak")

if __name__ == '__main__':
    main()