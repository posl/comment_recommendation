def is_wonderful(s):
    return len(s) == len(set(s)) and any(c.isupper() for c in s) and any(c.islower() for c in s)
