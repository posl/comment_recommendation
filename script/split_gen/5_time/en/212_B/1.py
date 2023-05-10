def main():
    pin = input()
    weak = True
    if pin[0] == pin[1] == pin[2] == pin[3]:
        weak = True
    else:
        for i in range(3):
            if pin[i+1] != str((int(pin[i]) + 1) % 10):
                weak = False
                break
    if weak:
        print("Weak")
    else:
        print("Strong")
