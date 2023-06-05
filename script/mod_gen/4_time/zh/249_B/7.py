def is_wonderful(s):
    if len(s) < 2:
        return "No"
    if s.islower() or s.isupper():
        return "No"
    if s[0].islower() and s[1].isupper():
        return "No"
    if s[0].isupper() and s[1].islower():
        return "No"
    if s[0].isupper():
        for i in range(1, len(s), 2):
            if s[i].isupper():
                return "No"
            if s[i].islower():
                continue
            else:
                return "No"
    if s[0].islower():
        for i in range(1, len(s), 2):
            if s[i].islower():
                return "No"
            if s[i].isupper():
                continue
            else:
                return "No"
    return "Yes"

if __name__ == '__main__':
    is_wonderful()