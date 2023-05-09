def checkWeakOrStrong(password):
    if password[0] == password[1] and password[1] == password[2] and password[2] == password[3]:
        print("Weak")
        return
    if int(password[0]) == 9 and int(password[1]) == 0 and int(password[2]) == 1 and int(password[3]) == 2:
        print("Weak")
        return
    if int(password[0]) == 8 and int(password[1]) == 9 and int(password[2]) == 0 and int(password[3]) == 1:
        print("Weak")
        return
    if int(password[0]) == 7 and int(password[1]) == 8 and int(password[2]) == 9 and int(password[3]) == 0:
        print("Weak")
        return
    if int(password[0]) == 6 and int(password[1]) == 7 and int(password[2]) == 8 and int(password[3]) == 9:
        print("Weak")
        return
    if int(password[0]) == 5 and int(password[1]) == 6 and int(password[2]) == 7 and int(password[3]) == 8:
        print("Weak")
        return
    if int(password[0]) == 4 and int(password[1]) == 5 and int(password[2]) == 6 and int(password[3]) == 7:
        print("Weak")
        return
    if int(password[0]) == 3 and int(password[1]) == 4 and int(password[2]) == 5 and int(password[3]) == 6:
        print("Weak")
        return
    if int(password[0]) == 2 and int(password[1]) == 3 and int(password[2]) == 4 and int(password[3]) == 5:
        print("Weak")
        return
    if int(password[0]) == 1 and int(password[1]) == 2 and int(password[2]) == 3 and int(password[3]) == 4:
        print("Weak")
        return
    if int(password[0]) == 0 and int(password[1]) == 1 and int(password[2]) == 2 and int(password[3]) == 3:
        print("
