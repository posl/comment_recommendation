def get_index(s):
    # 1位数
    if len(s) == 1:
        return ord(s) - ord('A') + 1
    # 2位数
    if len(s) == 2:
        return 26 + (ord(s[0]) - ord('A')) * 26 + (ord(s[1]) - ord('A') + 1)
    # 3位数
    if len(s) == 3:
        return 26 + 26 * 26 + (ord(s[0]) - ord('A')) * 26 * 26 + (ord(s[1]) - ord('A')) * 26 + (ord(s[2]) - ord('A') + 1)
    # 4位数
    if len(s) == 4:
        return 26 + 26 * 26 + 26 * 26 * 26 + (ord(s[0]) - ord('A')) * 26 * 26 * 26 + (ord(s[1]) - ord('A')) * 26 * 26 + (ord(s[2]) - ord('A')) * 26 + (ord(s[3]) - ord('A') + 1)
    # 5位数
    if len(s) == 5:
        return 26 + 26 * 26 + 26 * 26 * 26 + 26 * 26 * 26 * 26 + (ord(s[0]) - ord('A')) * 26 * 26 * 26 * 26 + (ord(s[1]) - ord('A')) * 26 * 26 * 26 + (ord(s[2]) - ord('A')) * 26 * 26 + (ord(s[3]) - ord('A')) * 26 + (ord(s[4]) - ord('A') + 1)
    # 6位数
    if len(s) == 6:
        return 26 + 26 * 26 + 26 * 26 * 26 + 26 * 26 * 26 * 26 + 26 * 26 * 26 * 26 * 26 + (ord(s[0]) - ord('A')) * 26 * 26 * 26 * 26 * 26 + (ord(s[
