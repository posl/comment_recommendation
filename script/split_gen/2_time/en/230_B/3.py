def is_substring_of_t(s):
    t = "oxx" * 10**5
    if s in t:
        return "Yes"
    else:
        return "No"
s = input()
print(is_substring_of_t(s))
