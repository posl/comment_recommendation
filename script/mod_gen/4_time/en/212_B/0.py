def main():
    pin = input()
    weak = True
    if pin[0] == pin[1] and pin[1] == pin[2] and pin[2] == pin[3]:
        weak = True
    else:
        weak = False
        for i in range(3):
            if (int(pin[i])+1)%10 != int(pin[i+1]):
                weak = True
                break
    if weak:
        print("Weak")
    else:
        print("Strong")

if __name__ == '__main__':
    main()