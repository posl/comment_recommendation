def get_index(s):
    if len(s) == 1:
        return ord(s) - ord('A') + 1
    else:
        return get_index(s[0]) * 26 + get_index(s[1:])
print(get_index(input()))
