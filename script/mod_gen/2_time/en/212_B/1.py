def main():
    pin = input()
    if pin[0] == pin[1] == pin[2] == pin[3]:
        print("Weak")
    elif pin[0] == pin[1] and pin[1] == pin[2]:
        print("Weak")
    elif pin[1] == pin[2] and pin[2] == pin[3]:
        print("Weak")
    elif pin[0] == pin[1] and pin[2] == pin[3]:
        print("Weak")
    elif pin[0] == str(int(pin[1])-1) and pin[1] == str(int(pin[2])-1) and pin[2] == str(int(pin[3])-1):
        print("Weak")
    elif pin[0] == "9" and pin[1] == "0" and pin[2] == "1" and pin[3] == "2":
        print("Weak")
    else:
        print("Strong")
main()

if __name__ == '__main__':
    main()