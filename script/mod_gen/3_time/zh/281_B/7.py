def check(s):
    if len(s) != 8:
        return False
    if s[0] < "A" or s[0] > "Z":
        return False
    if s[7] < "A" or s[7] > "Z":
        return False
    for i in range(1, 7):
        if s[i] < "0" or s[i] > "9":
            return False
    return True
s = input()

if __name__ == '__main__':
    check()