def is_easily_playable(s):
    if len(s) % 2 == 0:
        return False
    for i in range(0, len(s), 2):
        if s[i] in ['L', 'U', 'D']:
            pass
        else:
            return False
    for i in range(1, len(s), 2):
        if s[i] in ['R', 'U', 'D']:
            pass
        else:
            return False
    return True
