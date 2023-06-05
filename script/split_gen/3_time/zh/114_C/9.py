def is753(num):
    exist7 = False
    exist5 = False
    exist3 = False
    for i in str(num):
        if i == '7':
            exist7 = True
        elif i == '5':
            exist5 = True
        elif i == '3':
            exist3 = True
    if exist7 and exist5 and exist3:
        return True
    else:
        return False
