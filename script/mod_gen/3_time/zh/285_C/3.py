def get_index(s):
    index = 0
    for i in range(len(s)):
        index += (ord(s[i]) - 64) * 26 ** i
    return index
print(get_index(input()))
