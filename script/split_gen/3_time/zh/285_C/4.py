def get_num(s):
    num = 0
    for i in range(len(s)):
        num += (ord(s[i]) - 64) * (26 ** (len(s) - i - 1))
    return num
s = input()
print(get_num(s))
