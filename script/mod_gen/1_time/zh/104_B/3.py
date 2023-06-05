def check(s):
    if s[0] != 'A':
        return False
    if s[2:-1].count('C') != 1:
        return False
    if s.replace('A', '').replace('C', '').islower():
        return True
    else:
        return False

if __name__ == '__main__':
    check()