def get_id(s):
    if len(s) == 1:
        return ord(s) - ord('A') + 1
    else:
        return get_id(s[:-1]) * 26 + ord(s[-1]) - ord('A') + 1
s = input()
print(get_id(s))
