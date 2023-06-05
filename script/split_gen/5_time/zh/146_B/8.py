def move_char(c, n):
    if c.isalpha():
        if c.islower():
            return chr((ord(c) + n - ord('a')) % 26 + ord('a'))
        else:
            return chr((ord(c) + n - ord('A')) % 26 + ord('A'))
    else:
        return c
