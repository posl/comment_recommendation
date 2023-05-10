def main():
    pin = input()
    if pin[0] == pin[1] and pin[1] == pin[2] and pin[2] == pin[3]:
        print("Weak")
    elif (int(pin[1]) - int(pin[0]) == 1 or int(pin[1]) - int(pin[0]) == -9) and (int(pin[2]) - int(pin[1]) == 1 or int(pin[2]) - int(pin[1]) == -9) and (int(pin[3]) - int(pin[2]) == 1 or int(pin[3]) - int(pin[2]) == -9):
        print("Weak")
    else:
        print("Strong")

if __name__ == '__main__':
    main()