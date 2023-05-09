def main():
    #input
    pin = input()
    #compute
    if pin[0] == pin[1] == pin[2] == pin[3]:
        ans = 'Weak'
    elif int(pin[0]) == int(pin[1])-1 and int(pin[1]) == int(pin[2])-1 and int(pin[2]) == int(pin[3])-1:
        ans = 'Weak'
    elif int(pin[0]) == 9 and int(pin[1]) == 0 and int(pin[2]) == 1 and int(pin[3]) == 2:
        ans = 'Weak'
    else:
        ans = 'Strong'
    #output
    print(ans)
main()
