def checkString(string):
    if string[0].isupper() and string[-1].isupper():
        string = string[1:-1]
        if len(string) == 6 and string.isdigit() and 100000 <= int(string) <= 999999:
            return True
    return False
