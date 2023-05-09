def main():
    #input
    pin = input()
    #compute
    if pin[0] == pin[1] == pin[2] == pin[3]:
        ans = 'Weak'
    elif int(pin[0]) + 1 == int(pin[1]) or int(pin[0]) == 9 and int(pin[1]) == 0:
        if int(pin[1]) + 1 == int(pin[2]) or int(pin[1]) == 9 and int(pin[2]) == 0:
            if int(pin[2]) + 1 == int(pin[3]) or int(pin[2]) == 9 and int(pin[3]) == 0:
                ans = 'Weak'
            else:
                ans = 'Strong'
        else:
            ans = 'Strong'
    else:
        ans = 'Strong'
    #output
    print(ans)

if __name__ == '__main__':
    main()