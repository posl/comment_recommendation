def check_if_wonderful_string(string):
    if string.islower() or string.isupper():
        return False
    for i in string:
        if string.count(i) > 1:
            return False
    return True
