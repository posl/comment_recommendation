def get_index(s):
    if len(s) == 1:
        return ord(s) - ord('A') + 1
    else:
        count = 0
        for i in range(1, len(s)):
            count += 26 ** i
        count += ord(s[0]) - ord('A') + 1
        return count + get_index(s[1:])
