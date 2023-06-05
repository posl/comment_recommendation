def main():
    pin = input()
    weak = True
    if pin[0] == pin[1] and pin[1] == pin[2] and pin[2] == pin[3]:
        weak = True
    else:
        for i in range(3):
            if int(pin[i]) == 9 and int(pin[i+1]) == 0:
                weak = True
            elif int(pin[i]) + 1 == int(pin[i+1]):
                weak = True
            else:
                weak = False
                break
    if weak:
        print("Weak")
    else:
        print("Strong")
