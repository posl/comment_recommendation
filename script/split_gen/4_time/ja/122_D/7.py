def check(s):
    if "AGC" in s:
        return False
    for i in range(len(s)-1):
        if s[i:i+2] == "AGC":
            return False
    return True
