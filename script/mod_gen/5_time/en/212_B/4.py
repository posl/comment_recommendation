def problem():
    pin = input()
    if pin[0] == pin[1] == pin[2] == pin[3]:
        print("Weak")
        return
    for i in range(3):
        if (int(pin[i])+1)%10 != int(pin[i+1]):
            print("Strong")
            return
    print("Weak")
    return
problem()

if __name__ == '__main__':
    problem()