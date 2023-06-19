def check(s):
    if s[0] != 'A':
        return False
    if s[2:-1].count('C') != 1:
        return False
    for i in range(len(s)):
        if i == 0 or i == 2 or i == len(s) - 1:
            continue
        if s[i] < 'a' or s[i] > 'z':
            return False
    return True
s = input()

if __name__ == '__main__':
    check()