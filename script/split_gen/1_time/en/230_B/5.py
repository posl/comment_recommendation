def is_substring(s):
    t = "oxx" * 100000
    return "Yes" if s in t else "No"
s = input()
print(is_substring(s))
