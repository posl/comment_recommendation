def find_inserted_character_position(s, t):
    if len(s) == len(t):
        return -1
    else:
        for i in range(len(s)):
            if s[i] != t[i]:
                return i + 1
        return len(s) + 1
