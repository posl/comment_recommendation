def is_coffee_like(s):
    if s[2] == s[3] and s[4] == s[5]:
        return "Yes"
    return "No"
s = input()
print(is_coffee_like(s))
