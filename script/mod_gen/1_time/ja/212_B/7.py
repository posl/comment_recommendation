def main():
    password = list(input())
    if password[0] == password[1] and password[1] == password[2] and password[2] == password[3]:
        print('Weak')
    else:
        if password[0] == '9' and password[1] == '0' and password[2] == '1' and password[3] == '2':
            print('Weak')
        else:
            if int(password[1]) == (int(password[0]) + 1) % 10 and int(password[2]) == (int(password[1]) + 1) % 10 and int(password[3]) == (int(password[2]) + 1) % 10:
                print('Weak')
            else:
                print('Strong')

if __name__ == '__main__':
    main()