def is_prefix(s,t):
    if len(s) > len(t):
        return False
    if s == t[:len(s)]:
        return True
    else:
        return False

if __name__ == '__main__':
    is_prefix()