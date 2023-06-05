def is_wonderful_string(string):
    if len(string) < 2:
        return False
    if len(string) == 2:
        return string[0] != string[1]
    if len(string) % 2 == 1:
        return False
    if string[0].isupper():
        return False
    if string[-1].islower():
        return False
    if string[0].islower() and string[-1].isupper():
        return False
    return True

if __name__ == '__main__':
    is_wonderful_string()