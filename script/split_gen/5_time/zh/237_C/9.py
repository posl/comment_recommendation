def is_palindromic(s):
    if len(s) == 0:
        return False
    if len(s) == 1:
        return True
    if len(s) == 2:
        return s[0] == s[1]
    if len(s) == 3:
        return s[0] == s[2]
    if len(s) == 4:
        return s[0] == s[3] and s[1] == s[2]
    if len(s) == 5:
        return s[0] == s[4] and s[1] == s[3]
    if len(s) == 6:
        return s[0] == s[5] and s[1] == s[4] and s[2] == s[3]
    if len(s) == 7:
        return s[0] == s[6] and s[1] == s[5] and s[2] == s[4]
    if len(s) == 8:
        return s[0] == s[7] and s[1] == s[6] and s[2] == s[5] and s[3] == s[4]
    if len(s) == 9:
        return s[0] == s[8] and s[1] == s[7] and s[2] == s[6] and s[3] == s[5]
    if len(s) == 10:
        return s[0] == s[9] and s[1] == s[8] and s[2] == s[7] and s[3] == s[6] and s[4] == s[5]
    if len(s) == 11:
        return s[0] == s[10] and s[1] == s[9] and s[2] == s[8] and s[3] == s[7] and s[4] == s[6]
    if len(s) == 12:
        return s[0] == s[11] and s[1] == s[10] and s[2] == s[9] and s[3] == s[8] and s[4] == s[7] and s[5] == s
