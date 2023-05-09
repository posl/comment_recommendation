def check_ac(s):
    if s[0] != 'A':
        return False
    if s[2:-1].count('C') != 1:
        return False
    if not s[1:].replace('C', '').islower():
        return False
    return True
