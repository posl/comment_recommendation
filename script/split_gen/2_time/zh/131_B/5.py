def isDifficultToInput(password):
    if password[0] == password[1] and password[1] == password[2] and password[2] == password[3]:
        return True
    elif password[0] != password[1] and password[1] != password[2] and password[2] != password[3]:
        return True
    else:
        return False
