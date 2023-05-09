def check(s):
    if s[0] != "A":
        return False
    if s[2:-1].count("C") != 1:
        return False
    if s[1:].lower() != s[1:]:
        return False
    if s[2:-1].replace("C", "").lower() != s[2:-1].replace("C", ""):
        return False
    return True
s = input()
