def main():
    pin = input()
    if pin[0] == pin[1] == pin[2] == pin[3]:
        print("Weak")
    elif pin[1] == str((int(pin[0])+1)%10) and pin[2] == str((int(pin[1])+1)%10) and pin[3] == str((int(pin[2])+1)%10):
        print("Weak")
    else:
        print("Strong")

if __name__ == '__main__':
    main()