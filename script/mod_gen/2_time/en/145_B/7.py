def is_concatenation(s):
    if len(s) % 2 == 0:
        if s[:len(s)//2] == s[len(s)//2:]:
            return True
    return False

if __name__ == '__main__':
    is_concatenation()