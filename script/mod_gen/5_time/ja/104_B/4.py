def is_ac(s):
    if s[0] != "A":
        return False
    if s[1:].count("C") != 1:
        return False
    for i in range(2, len(s)-1):
        if s[i] == "C":
            return False
    for i in range(len(s)):
        if s[i] == "A" or s[i] == "C":
            continue
        if s[i].isupper():
            return False
    return True
s = input()

if __name__ == '__main__':
    is_ac()