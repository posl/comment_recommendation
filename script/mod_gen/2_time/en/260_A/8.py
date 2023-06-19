def single_char(s):
    """Return the single character in 's' or -1 if no such character."""
    for c in s:
        if s.count(c) == 1:
            return c
    return -1
s = input()
print(single_char(s))
