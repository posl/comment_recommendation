def check_ac(s):
    if s[0] != 'A':
        return False
    if s[1] == 'C' or s[-2] == 'C':
        return False
    if s[2:-2].count('C') != 1:
        return False
    for i in s:
        if i != 'A' and i != 'C' and i.isupper():
            return False
    return True
s = input()

if __name__ == '__main__':
    check_ac()