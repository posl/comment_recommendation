def get_index(s):
    result = 0
    for i in range(len(s)):
        result += (ord(s[i]) - ord('A') + 1) * 26 ** (len(s) - i - 1)
    return result
