def check(s):
    if s[0] != "A":
        return False
    if s[2:-1].count("C") != 1:
        return False
    for i in range(len(s)):
        if i == 0:
            continue
        if s[i] == "A":
            continue
        if s[i] == "C":
            continue
        if s[i].islower():
            continue
        return False
    return True
s = input()

if __name__ == '__main__':
    check()