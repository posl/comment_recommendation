def check_string(s, t):
    if len(t) > len(s):
        return False
    if t in s:
        return True
    else:
        return False

if __name__ == '__main__':
    check_string()