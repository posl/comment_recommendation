def check_str(s):
    if s[0] == 'A' and s[2:-1].count('C') == 1 and s[1:].islower():
        return True
    else:
        return False
