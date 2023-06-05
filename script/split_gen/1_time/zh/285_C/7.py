def find_index(s):
    # 用26进制的思想
    index = 0
    for i in range(len(s)):
        index = index * 26 + ord(s[i]) - ord('A') + 1
    return index
