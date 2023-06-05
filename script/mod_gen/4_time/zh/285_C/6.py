def convert(s):
    num = 0
    for i in range(len(s)):
        num *= 26
        num += ord(s[i]) - ord('A') + 1
    return num
print(convert(input()))
