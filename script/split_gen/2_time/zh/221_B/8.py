def is_anagram(s, t):
    if len(s) == len(t):
        if sorted(s) == sorted(t):
            return True
    return False
