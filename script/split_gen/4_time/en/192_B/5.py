def solve():
    s = input()
    for i, c in enumerate(s):
        if i % 2 == 0:
            if c.islower():
                continue
            else:
                return False
        else:
            if c.isupper():
                continue
            else:
                return False
    return True
