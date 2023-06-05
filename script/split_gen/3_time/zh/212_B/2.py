def main():
    pin = input()
    if pin[0] == pin[1] and pin[1] == pin[2] and pin[2] == pin[3]:
        print("Weak")
    else:
        flag = True
        for i in range(3):
            if pin[i] == '9':
                if pin[i+1] != '0':
                    flag = False
                    break
            else:
                if int(pin[i]) + 1 != int(pin[i+1]):
                    flag = False
                    break
        if flag:
            print("Weak")
        else:
            print("Strong")
