def check_string(s):
    if s.islower():
        return False
    if s.isupper():
        return False
    if len(set(s)) != len(s):
        return False
    return True

if __name__ == '__main__':
    check_string()