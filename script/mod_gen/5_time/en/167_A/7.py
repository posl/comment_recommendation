def check_string(s,t):
    if len(s) == len(t) - 1:
        if s == t[:-1]:
            return True
    return False

if __name__ == '__main__':
    check_string()