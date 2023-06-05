def is_wonderful_string(string):
    if not string:
        return False
    if len(string) == 1:
        return False
    if len(string) == 2:
        if string[0].islower() and string[1].isupper():
            return True
        else:
            return False
    if len(string) > 2:
        if string[0].islower() and string[1].isupper():
            for i in range(2, len(string)):
                if string[i].islower():
                    return False
            return True
        if string[0].isupper() and string[1].islower():
            for i in range(2, len(string)):
                if string[i].isupper():
                    return False
            return True
        return False

if __name__ == '__main__':
    is_wonderful_string()