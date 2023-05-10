def func(n):
    l = len(n)
    if l == 1:
        if int(n) % 3 == 0:
            return 0
        else:
            return -1
    elif l == 2:
        if int(n) % 3 == 0:
            return 0
        elif int(n[0]) % 3 == 0 or int(n[1]) % 3 == 0:
            return 1
        else:
            return -1
    elif l == 3:
        if int(n) % 3 == 0:
            return 0
        elif int(n[0]) % 3 == 0 and int(n[1]) % 3 == 0:
            return 1
        elif int(n[0]) % 3 == 0 and int(n[2]) % 3 == 0:
            return 1
        elif int(n[1]) % 3 == 0 and int(n[2]) % 3 == 0:
            return 1
        elif int(n[0]) % 3 == 0 or int(n[1]) % 3 == 0 or int(n[2]) % 3 == 0:
            return 2
        else:
            return -1
    else:
        if int(n) % 3 == 0:
            return 0
        elif int(n[0]) % 3 == 0 and int(n[1]) % 3 == 0 and int(n[2]) % 3 == 0:
            return 1
        elif int(n[0]) % 3 == 0 and int(n[1]) % 3 == 0 and int(n[3]) % 3 == 0:
            return 1
        elif int(n[0]) % 3 == 0 and int(n[2]) % 3 == 0 and int(n[3]) % 3 == 0:
            return 1
        elif int(n[1]) % 3 == 0 and int(n[2]) % 3 == 0 and int(n[3]) % 3 == 0:
            return 1
        elif int(n[0]) % 3 == 0 and int(n[1]) % 3 == 0:
            return 2
        elif int(n[
