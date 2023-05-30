def is_wonderful_string(s):
    if len(s) < 2:
        return "No"
    if len(s) > 100:
        return "No"
    if s.islower():
        return "No"
    if s.isupper():
        return "No"
    if len(s) != len(set(s)):
        return "No"
    return "Yes"
print(is_wonderful_string(input()))
