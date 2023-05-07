def is_hard_to_read(s):
    for i in range(len(s)):
        if i % 2 == 0:
            if not s[i].isupper():
                return False
        else:
            if not s[i].islower():
                return False
    return True
s = input()
