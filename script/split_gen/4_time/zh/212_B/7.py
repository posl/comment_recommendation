def main():
    pin = input()
    weak = True
    for i in range(3):
        if pin[i] != pin[i+1]:
            weak = False
            break
    if weak:
        print("Weak")
        return
    weak = True
    for i in range(3):
        if int(pin[i]) != (int(pin[i+1]) + 1) % 10:
            weak = False
            break
    if weak:
        print("Weak")
    else:
        print("Strong")
