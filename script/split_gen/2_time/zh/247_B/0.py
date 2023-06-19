def checkName(name):
    for i in range(len(name)):
        if name[i] == " ":
            return False
    return True
