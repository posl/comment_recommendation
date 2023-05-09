def problem():
    pin = input()
    weak = True
    if pin[0] == pin[1] == pin[2] == pin[3]:
        weak = True
    else:
        for i in range(3):
            if pin[i] == '9':
                if pin[i+1] != '0':
                    weak = False
                    break
            else:
                if int(pin[i])+1 != int(pin[i+1]):
                    weak = False
                    break
    if weak:
        print('Weak')
    else:
        print('Strong')
problem()

if __name__ == '__main__':
    problem()