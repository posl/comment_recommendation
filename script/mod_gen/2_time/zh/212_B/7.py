def main():
    pin = input()
    if pin.count(pin[0]) == 4 or pin[0] == '9' and pin[1] == '0' and pin[2] == '1' and pin[3] == '2' or pin[0] == '0' and pin[1] == '1' and pin[2] == '2' and pin[3] == '3' or pin[0] == '1' and pin[1] == '2' and pin[2] == '3' and pin[3] == '4' or pin[0] == '2' and pin[1] == '3' and pin[2] == '4' and pin[3] == '5' or pin[0] == '3' and pin[1] == '4' and pin[2] == '5' and pin[3] == '6' or pin[0] == '4' and pin[1] == '5' and pin[2] == '6' and pin[3] == '7' or pin[0] == '5' and pin[1] == '6' and pin[2] == '7' and pin[3] == '8' or pin[0] == '6' and pin[1] == '7' and pin[2] == '8' and pin[3] == '9' or pin[0] == '7' and pin[1] == '8' and pin[2] == '9' and pin[3] == '0':
        print("Weak")
    else:
        print("Strong")

if __name__ == '__main__':
    main()